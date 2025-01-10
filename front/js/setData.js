const month = [
    'Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря', 
]

let currentDate = new Date();

function ChangeCurretData(selector = ".date") {
    currentDate = new Date()
    document.querySelector(".date").innerHTML = currentDate.getDate() + " " + month[currentDate.getMonth()] + " " + currentDate.getFullYear()
}

ChangeCurretData()