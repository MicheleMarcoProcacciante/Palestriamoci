fetch('http://192.168.0.124:5000/getLogin')
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => console.error('Ошибка:', error))





// chartLib.makeChart(chart_data)
