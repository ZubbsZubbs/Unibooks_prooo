document.addEventListener('DOMContentLoaded', function () {
    const welcomeButton = document.getElementById('welcomeButton');
    if (welcomeButton) {
        welcomeButton.addEventListener('click', function () {
            alert('Welcome to Our Book Reading App! Enjoy our vast selection of books.');
        });
    }
});
