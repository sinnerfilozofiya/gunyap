console.log("burayı buluyor musun acaba")

degree=0
function rotateImage(imageId, degrees) {
    degree+=degrees
    console.log("giriyor musun buraya")
    var img = document.getElementById('img-preview-' + imageId);
    if (img) {
        img.style.transform = 'rotate(' + degree + 'deg)';
    }
}


