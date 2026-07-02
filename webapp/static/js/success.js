const closeButton = document.querySelector(".close")

closeButton.onclick = returnToForm

function returnToForm() {
    window.location.href = "form.html"
    console.log(closeButton)
}