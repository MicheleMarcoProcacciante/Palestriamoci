fetch('http://192.168.1.15:5000/showcards')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Здесь код для отображения данных в вашем HTML
    })
    .catch(error => console.error('Ошибка:', error));
