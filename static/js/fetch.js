fetch('http://192.168.0.134:5000/api/data')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Здесь код для отображения данных в вашем HTML
    })
    .catch(error => console.error('Ошибка:', error));
