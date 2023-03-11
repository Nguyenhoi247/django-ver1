// validation form register and register user local storage
const inputNameRegister = document.querySelector(".text-name");
const inputEmailRegister = document.querySelector(".email");
const inputPasswordRegister = document.querySelector(".password");
const btnRegister = document.querySelector(".btn-up");

// validation form register and register user local storage

btnRegister.addEventListener("click", (e) => {
  e.preventDefault();
  if (
    inputEmailRegister.value === "" ||
    inputPasswordRegister.value === ""
  ) {
    alert("vui lòng không để trống");
  } else {
    // array user
    const user = {
      username: inputEmailRegister.value,
      password: inputPasswordRegister.value,
    };
    let json = JSON.stringify(user);
    localStorage.setItem(inputEmailRegister.value, json);
    alert("Đăng Ký Thành Công");
    window.location.href = "login.html";
  }
});