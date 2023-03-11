var modal = document.getElementById('create-post-popup');
var btn = document.getElementById('create-post-button');
var span = document.getElementsByClassName('popup-close')[0];


btn.onclick = function () {
    modal.style.display = 'block';
}

span.onclick = function () {
    modal.style.display = 'none';
}

// window.onclick = function (event) {
//     if (event.target == modal) {
//         modal.style.display = 'none';
//     }
// }

