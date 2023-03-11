const inputName = document.querySelector(".login-name");
const inputPassword = document.querySelector(".login-password");
const btnLogin = document.querySelector(".btn-login");


btnLogin.addEventListener("click", (e) => {
    e.preventDefault();
    if (inputName.value === "" || inputPassword.value === "") {
        alert("bạn còn nhập thiếu");
    } else {
        const user = JSON.parse(localStorage.getItem(inputName.value));
        if (
            user.username === inputName.value &&
            user.password === inputPassword.value
        ) {
            alert("Đăng nhập thành công");
            window.location.href = "index.html";
        } else {
            alert("Đăng nhập thất bại");
        }
    }
});