from athletesInfoFull import Athletes
# from athletesInfoShared import AthletesInfoShared
from trainingCards import TrainingCards
from cardsComposition import CardsComposition
from flask import Flask, request, render_template, redirect, url_for, session
from flask_session import Session
import pymysql
import json

app = Flask(__name__, static_url_path='/static')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

connection = pymysql.connect(host="localhost", user="root", password="XCqgtecl06!", database="palestriamocidb", port=3306, autocommit=True)

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
    

@app.route('/templates/log-in.html?#logo_log-in', methods = ['POST'])
def login():
    
    email = request.form.get('inputEmail')
    password = request.form.get('inputPassword')
    # email = request.form['inputEmail']
    # password = request.form['inputPassword']

    atleta = None

    try:
        sql = "select * from athletes where email = '%s' AND password_ = '%s'" % (email,password)
        cursor.execute(sql)
        row = cursor.fetchone()

        atleta = Athletes (row[0],row[1],row[2],row[3],row[4],row[5])        

        session["id_loggeduser"] = atleta.id


        return redirect ("/account")
    
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

'''  per android
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
'''

''' NO
# PER SITO WEB
@app.route('/showcards', methods = ['GET'])
def showCard():

# id utente, vede tutte schede in base a id utente. vedo tutti i card composition di tutte le schede.

    # id = session["id_loggeduser"]
    id = 1

    sql = """select trainingCards.trainingCards_id, athletes.athletes_id, trainingCards.name_table, trainingCards.date_, cardsComposition.series, cardsComposition.reps, cardsComposition.loads,
            cardsComposition.rest, cardsComposition.duration, cardsComposition.comment_
            from trainingCards
	        left join athletes on trainingcards.athletes_fk = athletes.athletes_id
	        inner join cardsComposition on trainingCards.trainingCards_id = cardsComposition.trainingCards_fk
            where athletes.athletes_id = '%s'""" % (id)
    cursor.execute(sql)
    cards = cursor.fetchall()

    schede=[]

    numeroschede = 0

    for card in cards:
        scheda = TrainingCards (card[0],card[1],card[2],card[3])
        schede.append(scheda)
        numeroschede = numeroschede + 1

    # return json.dumps(schede, default=vars)
    return render_template("indexDELETE.html", datiSchede = schede, nSchede = numeroschede)
'''

# PER SITO WEB
@app.route('/showcards', methods = ['GET'])
def showCard():

# id utente, vede tutte schede in base a id utente. vedo tutti i card composition di tutte le schede.

    # id = session["id_loggeduser"]
    id = 1

    sql = """"select * from TrainingCards where athletes_fk = '%s'" % (id)""" % (id)
    cursor.execute(sql)
    cards = cursor.fetchall()

    schede=[]

    numeroschede = 0

    for card in cards:
        scheda = TrainingCards (card[0],card[1],card[2],card[3])
        schede.append(scheda)
        numeroschede = numeroschede + 1

    # return json.dumps(schede, default=vars)
    return render_template("indexDELETE.html", datiSchede = schede, nSchede = numeroschede)


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

    return redirect ("/account")

    #return render_template("buttare.html", datiHtmlNome = name, datiHtmlCognome = surname, datiHtmlEmail = email, datiHtmlPassword = password)


@app.route("/account")
def dettaglio():
    id = session["id_loggeduser"]

    sql = (f"select * from athletes where athletes_id = {id}")
    cursor.execute(sql)
    row = cursor.fetchone()
    
    atleta = Athletes (row[0],row[1],row[2],row[3],row[4],row[5])

    # Password non si vede perchè manca nel html, decidere come implementarla

    return render_template("my_account.html", athlete = atleta)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
