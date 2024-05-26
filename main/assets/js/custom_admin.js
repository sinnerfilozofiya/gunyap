degree=0
document.addEventListener('DOMContentLoaded', function () {
    const rotateButtons = document.querySelectorAll('.rotate-image-button');
    rotateButtons.forEach(button => {
        button.addEventListener('click', function () {
            const projectId = this.getAttribute('data-project-id'); 
            const imageId = this.getAttribute('data-image-id');
            let rotateUrl = this.getAttribute('data-rotate-url');
            // Rotate URL'yi güncelle
            console.log("image in id si",imageId)
            rotateUrl = rotateUrl.replace('0', imageId);
            const imageElement = document.querySelector(`#img-preview-${imageId}`);
            degree=degree+90
            imageElement.style.transform = 'rotate(' + degree + 'deg)';
            url=`/admin/proje/proje/${projectId}/change/${imageId}`
            // Döndürülmüş görüntüyü sunucuya gönder
            fetch(url,  {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ image_id: imageId,proje_id:projectId})
            })
            .then(response => {
                if (response.ok) {
                    console.log("url şu",url)
                    console.log('Görüntü başarıyla döndürüldü ve güncellendi.');
                } else {
                    console.error('Görüntü döndürülürken bir hata oluştu.');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});

// CSRF token almak için yardımcı işlev
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}