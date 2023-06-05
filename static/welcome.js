window.onload= function () {
    document.getElementById('hello').style.display= "block";
    openSignup();
}

  function openSignup() {
    setTimeout(() => {
      window.location.href = "/login";
    }, 5000);
  }


