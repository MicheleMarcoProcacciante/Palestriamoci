fetch('http://192.168.0.139:5000/showcardsJson')
    .then(response => response.json())
    .then(data => {
        data = getDataByGroup(data)
        let mainContainer = document.getElementById("mainContainer")
        if (data.length > 0) {
            Workout.createContainer(data, mainContainer); // Обратите внимание на изменения в аргументах
        }
    })
    .catch(error => console.error('Ошибка:', error))

class Exercise {
    constructor({ exercise_name, loads, reps, rest, duration, comment_ }) {
        this.exerciseName = exercise_name;
        this.loads = loads;
        this.reps = reps;
        this.rest = rest;
        this.duration = duration;
        this.comment = comment_;
    }
}

class Workout {
    constructor(id, name, date) {
        this.id = id
        this.name = name
        this.date = date
        this.exercises = []
    }

    addExercise(exercise) {
        this.exercises.push(new Exercise(exercise))
    }

    static createContainer(data, mainContainer) {
        console.log(data)

        for (let index = 0; index < data.length; index++) {
            const elSchedaBlock = document.createElement("div")
            elSchedaBlock.className = "scheda-block"
            const btnPrimary = document.createElement("button")
            btnPrimary.classList = "btn btn-primary btn_modal"
            btnPrimary.setAttribute("type", "button")
            btnPrimary.setAttribute("data-bs-toggle", "modal")
            btnPrimary.setAttribute("data-bs-target", `#exampleModal${[index]}`)

            const spanNameOfScheda = document.createElement("span")
            spanNameOfScheda.innerText = "Nome scheda: " + data[index].name

            const spanSeparator = document.createElement("span")
            spanSeparator.innerText = " / "

            const spanDateOfScheda = document.createElement("span")
            spanDateOfScheda.innerText = "Data Creazione: " + data[index].date
            btnPrimary.append(spanNameOfScheda)
            btnPrimary.append(spanSeparator)
            btnPrimary.append(spanDateOfScheda)

            elSchedaBlock.append(btnPrimary)

            const elModal = document.createElement("div")
            elModal.classList = "modal fade modal-dialog-scrollable"
            elModal.setAttribute("id", `exampleModal${[index]}`)
            elModal.setAttribute("tabindex", "-1")
            elModal.setAttribute("aria-labelledby", "exampleModalLabel")
            elModal.setAttribute("aria-hidden", "true")

            const elModalCnt = document.createElement("div")
            elModalCnt.classList = "modal-dialog modal_container"

            const elModalBox = document.createElement("div")
            elModalBox.classList = "modal-content modal_box"

            const elModalHeader = document.createElement("div")
            elModalHeader.classList = "modal-header info_scheda"
            const elModalHeaderNameOfScheda = document.createElement("h3")
            elModalHeaderNameOfScheda.innerText = "Nome scheda: " + data[index].name
            elModalHeaderNameOfScheda.classList = "modal-title title_modal fs-5"
            elModalHeaderNameOfScheda.setAttribute("id", "exampleModalLabel")
            const elModalHeaderDateOfScheda = document.createElement("h3")
            elModalHeaderDateOfScheda.innerText = "Nome scheda: " + data[index].date
            elModalHeaderDateOfScheda.classList = "modal-title title_modal fs-5"
            elModalHeaderDateOfScheda.setAttribute("id", "exampleModalLabel")
            elModalHeader.append(elModalHeaderNameOfScheda)
            elModalHeader.append(elModalHeaderDateOfScheda)

            const elModalBody = document.createElement("div")
            const elModalCommento = document.createElement("div")
            const elModalFooter = document.createElement("div")

            elModalBox.append(elModalHeader)
            elModalBox.append(elModalBody)
            elModalBox.append(elModalCommento)
            elModalBox.append(elModalFooter)
            elModalCnt.append(elModalBox)
            elModal.append(elModalCnt)
            elSchedaBlock.append(elModal)
            mainContainer.append(elSchedaBlock)
        }
    }
}

function getDataByGroup(data) {
    // Шаг 1: Группировка данных в объект с использованием id в качестве ключей
    const grouped = data.reduce((acc, item) => {
        if (!acc[item.id]) {
            acc[item.id] = [];
        }
        acc[item.id].push(item); // Добавляем объект целиком, предполагая, что это данные упражнения
        return acc;
    }, {});

    // Шаг 2: Преобразование объекта в массив массивов
    const result = Object.values(grouped).map(group => {
        // Для каждой группы создаем объект Workout, добавляем упражнения и возвращаем его
        const workout = new Workout(group[0].id, group[0].name, group[0].date);
        group.forEach(item => workout.addExercise(item));
        return workout;
    });

    return result;
}

