function validateForm() {
  var username = document.forms["loginForm"]["username"].value;
  var password = document.forms["loginForm"]["password"].value;
  if (username == "user" && password == "pass") {
    localStorage.setItem("loggedIn", true);
    document.getElementById("login").style.display = "none";
    document.getElementById("info").style.display = "block";
    return false;
  } else {
    alert("Wrong username or password");
    return false;
  }
}

window.onload = function() {
  if (localStorage.getItem("loggedIn")) {
    document.getElementById("login").style.display = "none";
    document.getElementById("info").style.display = "block";
  }
};

function submitForm(){
  document.getElementById("form-id").submit();
  setTimeout(function(){
    window.location.href = '/';
  }, 1000);
}