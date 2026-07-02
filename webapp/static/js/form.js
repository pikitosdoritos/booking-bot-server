const fullnameInput = document.getElementById("fullname")
const phoneInput = document.getElementById("phone-number")
const dateInput = document.getElementById("datetime")
const btn = document.querySelector(".check")

btn.onclick = validateForm

function validateForm() {
    const name = fullnameInput.value
    const phone = phoneInput.value
    const date = dateInput.value

    const validityErrors = [checkName(name), checkPhone(phone), checkDate(date)]

    showInvalid(validityErrors)
}

function checkName(name) {
    if (!/\w{2,}(-\w{2,})? \w{2,}(-\w{2,})?/.test(name)) {
        return "Укажите ФИО"
    }
}

function checkPhone(phone) {
    if (!/\+\d{1,3} ?\(\d{2}\) ?\d{3}-?\d{2}-?\d{2}/.test(phone)) {
        return "Введите корректный номер телефона"
    }
}

function checkDate(date) {
    if (!date) {
        return "Выберите дату тренировки"
    }
}

function showInvalid(validityErrors) {
    const inputs = [fullnameInput, phoneInput, dateInput]

    for (let i = 0; i < 3; i++) {
        const p = inputs[i].nextElementSibling?.closest("p")

        if (p) p.remove()

        if (validityErrors[i]) {
            const hint = document.createElement("p")
            
            hint.append(validityErrors[i])

            inputs[i].classList.add("invalid")
            inputs[i].after(hint)
        } else {
            inputs[i].classList.remove("invalid")
        }
    }
}