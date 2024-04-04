fetch('http://127.0.0.1:5000/showcardsJson')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        data = getDataByGroup(data)
        let mainContainer = document.getElementById("mainContainer")
        if (data.length > 0) {
            Workout.createContainer(data, mainContainer); // Обратите внимание на изменения в аргументах
        }
    })
    .catch(error => console.error('Ошибка:', error))

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
        const workout = new Workout(group[0].id, group[0].name, group[0].date, group[0].comment_);
        group.forEach(item => workout.addExercise(item));
        return workout;
    });

    return result;
}

class Exercise {
    constructor({ exercise_name, loads, series, reps, rest, duration }) {
        this.exerciseName = exercise_name;
        this.loads = loads;
        this.series = series;
        this.reps = reps;
        this.rest = rest;
        this.duration = duration;
    }

    static createTableExercises(data) {
        const modalTable = document.createElement("table")
        modalTable.classList = "modal_table"

        const trRowName = document.createElement("tr")
        trRowName.classList = "col row-name"

        const thRowNameEsercizio = document.createElement("th")
        thRowNameEsercizio.innerText = "Esercizio"
        trRowName.append(thRowNameEsercizio)

        const thRowNameSerie = document.createElement("th")
        thRowNameSerie.innerText = "Serie (N°)"
        trRowName.append(thRowNameSerie)

        const thRowNameRipetiz = document.createElement("th")
        thRowNameRipetiz.innerText = "Ripetiz. (N°)"
        trRowName.append(thRowNameRipetiz)

        const thRowNameCarico = document.createElement("th")
        thRowNameCarico.innerText = "Carico (KG)"
        trRowName.append(thRowNameCarico)

        const thRowNameRipresa = document.createElement("th")
        thRowNameRipresa.innerText = "Ripresa (min)"
        trRowName.append(thRowNameRipresa)

        const thRowNameDurata = document.createElement("th")
        thRowNameDurata.innerText = "Durata Esercizio (min)"
        trRowName.append(thRowNameDurata)
        modalTable.append(trRowName)

        for (let index = 0; index < data.length; index++) {
            const trRow = document.createElement("tr")
            trRow.classList = "col row-name"
            const thRowEsercizio = document.createElement("th")
            thRowEsercizio.innerText = data[index].exerciseName
            trRow.append(thRowEsercizio)

            const tdRowSerie = document.createElement("td")
            tdRowSerie.innerText = data[index].series
            trRow.append(tdRowSerie)

            const tdRowRipetiz = document.createElement("td")
            tdRowRipetiz.innerText = data[index].reps
            trRow.append(tdRowRipetiz)

            const tdRowCarico = document.createElement("td")
            tdRowCarico.innerText = data[index].loads
            trRow.append(tdRowCarico)

            const tdRowRipresa = document.createElement("td")
            tdRowRipresa.innerText = data[index].rest
            trRow.append(tdRowRipresa)

            const tdRowDurata = document.createElement("td")
            tdRowDurata.innerText = data[index].duration
            trRow.append(tdRowDurata)

            modalTable.append(trRow)
        }

        return modalTable
    }
}

class Workout {
    constructor(id, name, date, comment_) {
        this.id = id
        this.name = name
        this.date = date
        this.comment = comment_;
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
            elModalHeaderDateOfScheda.innerText = "Data Creazione: " + data[index].date
            elModalHeaderDateOfScheda.classList = "modal-title title_modal fs-5"
            elModalHeaderDateOfScheda.setAttribute("id", "exampleModalLabel")
            elModalHeader.append(elModalHeaderNameOfScheda)
            elModalHeader.append(elModalHeaderDateOfScheda)

            const elModalBody = document.createElement("div")
            elModalBody.classList = "modal-body container_modal_body"

            const tableExercises = Exercise.createTableExercises(data[index].exercises)

            elModalBody.append(tableExercises)

            const elModalCommento = document.createElement("div")
            elModalCommento.classList = "commento container"
            const titleCommento = document.createElement("h2")
            titleCommento.innerText = "Commento"
            elModalCommento.append(titleCommento)
            const testoCommento = document.createElement("p")
            testoCommento.classList = "p_commento"
            testoCommento.innerText = data[index].comment

            elModalCommento.append(testoCommento)

            const elModalFooter = document.createElement("div")
            elModalFooter.classList = "modal-footer"

            const footerBtn = document.createElement("button")
            footerBtn.classList = "btn btn-secondary"
            footerBtn.setAttribute("data-bs-dismiss", "modal")
            footerBtn.innerText = "Close"
            elModalFooter.append(footerBtn)

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



