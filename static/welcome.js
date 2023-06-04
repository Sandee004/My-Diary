window.onload= function () {
    document.getElementById('hello').style.display= "block";
    openSignup();
}


  function openSignup() {
    setTimeout(() => {
      window.location.href = "/intro";
    }, 5000);
  }