from athletesInfoFull import Athletes
from athletesInfoShared import AthletesInfoShared
from trainingCards import TrainingCards
from cardsComposition import CardsComposition
from flask import Flask, request, render_template, redirect, url_for, session
from flask_session import Session
import pymysql
import json

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

connection = pymysql.connect(host="localhost", user="root", password="root", database="palestriamocidb", port=3306, autocommit=True)

cursor = connection.cursor()

''' vecchio codice per capire
@app.route('/login', methods = ['GET'])
def login():
    # forms.get
    email = request.args.get('email')
    password = request.args.get('password_')

    atleta = None

    try:
        sql = "select * from athletes where email = '%s' AND password_ = '%s'" % (email,password)
        cursor.execute(sql)
        row = cursor.fetchone()

        atleta = Athletes (row[0],row[1],row[2],row[3],row[4],row[5])
    except:
        # notifica di errore
        print ("Account non trovato")
    return json.dumps(atleta, default=vars)
'''

@app.route('/login', methods = ['GET'])
def getLogin():
    return render_template("log-in.html", )
    

@app.route('/login', methods = ['POST'])
def login():
    
    email = request.form.get('inputEmail')
    password = request.form.get('inputPassword')

    atleta = None

    try:
        sql = "select * from athletes where email = '%s' AND password_ = '%s'" % (email,password)
        cursor.execute(sql)
        row = cursor.fetchone()

        atleta = Athletes (row[0],row[1],row[2],row[3],row[4],row[5])

        session["id_loggeduser"] = atleta.id


        return redirect ("/homepage")
    
    except:
        # notifica di errore
        print ("Account non trovato")
    return json.dumps(atleta, default=vars)


@app.route('/cardsComposition', methods = ['GET'])
def showCardComposition():
    
    id = request.args.get('trainingCards_id')
    sql = """select exercises.exercise_name, trainingCards.date_, cardsComposition.series, cardsComposition.reps,
                cardsComposition.loads, cardsComposition.rest, cardsComposition.duration, cardsComposition.comment_
                from exercises 
                    inner join cardsComposition on cardsComposition.exercises_fk = exercises.exercises_id
                    inner join trainingCards on cardsComposition.trainingCards_fk = trainingCards.trainingCards_id
                where trainingCards.trainingCards_id = '%s'""" % (id)

    cursor.execute(sql)
    righe = cursor.fetchall()

    allenamentiGiornata = []

    for elemento in righe:
        allenamentoGiornata = CardsComposition (elemento[0],elemento[1],elemento[2],elemento[3],elemento[4],elemento[5],elemento[6],elemento[7])
        allenamentiGiornata.append(allenamentoGiornata)

    return json.dumps(allenamentiGiornata, default=vars)


@app.route('/showcards', methods = ['GET'])
def showCard():

    # id = session["id_loggeduser"] 
    id = 1

    sql = ("select * from TrainingCards where athletes_fk = '%s'" % (id))
    cursor.execute(sql)
    cards = cursor.fetchall()

    schede=[]

    numeroschede = 0

    for card in cards:
        scheda = TrainingCards (card[0],card[1],card[2],card[3])
        schede.append(scheda)
        numeroschede = numeroschede + 1

    # return json.dumps(schede, default=vars)
    return render_template("indexDELETE.html", datiScheda = scheda, nSchede = numeroschede)


@app.route('/register', methods = ['GET'])
def getRegister():
    return render_template("sign-in.html", )


@app.route('/register', methods = ['POST'])
def register():

    email = request.form['inputEmail']
    password = request.form['inputPassword']
    name = request.form['inputNome']
    surname = request.form['inputCognome']
    date_of_birth = request.form['inputDate']

    cursor.execute(f"""insert into athletes (email, password_, name_, surname, date_of_birth) values ('{email}', '{password}',
                '{name}','{surname}','{date_of_birth}')""")
    
    # capire cosa serve
    cursor.connection.commit()

    session["id_loggeduser"] = cursor.lastrowid

    return redirect ("/homepage")

    #return render_template("buttare.html", datiHtmlNome = name, datiHtmlCognome = surname, datiHtmlEmail = email, datiHtmlPassword = password)


@app.route("/homepage")
def dettaglio():
    id = session["id_loggeduser"]

    sql = f"select * from athletes where athletes_id = {id}"
    cursor.execute(sql)
    row = cursor.fetchone()
    
    atleta = AthletesInfoShared (row[0],row[1],row[2],row[3],row[4])

    return render_template("index.html", athlete = atleta)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
