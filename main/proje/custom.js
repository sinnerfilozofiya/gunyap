function rotateImage(button) {
    var row = button.closest('.form-row');
    var image = row.querySelector('img');
    image.style.transform = 'rotate(90deg)';
}
