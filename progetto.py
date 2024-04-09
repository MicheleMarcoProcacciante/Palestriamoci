from athletesInfoFull import Athletes
# from athletesAPI import AthletesApi
from trainingCardsWeb import TrainingCardsWeb
from trainingCardsAndroid import TrainingCardsAndroid
from cardsComposition import CardsComposition
from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from flask_session import Session
import pymysql
import json

app = Flask(__name__, static_url_path='/static')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

connection = pymysql.connect(host="localhost", user="root", password="NUOVAPASSWORD", database="palestriamocidb", port=3306, autocommit=True)

cursor = connection.cursor()



@app.route('/index')
def getIndex():
    return render_template("index.html", )



# endpoint
@app.route('/logout', methods = ['GET'])
def getLogout():
    session["id_loggeduser"] = None
    return redirect("/index")

@app.route('/login', methods = ['GET'])
def getLogin():
    return render_template("log-in.html", loginError = False)


@app.route('/login', methods = ['POST'])
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

        if row != None:
            atleta = Athletes (row[0],row[1],row[2],row[3],row[4],row[5])        

            # print(atleta.date_of_birth)

            session["id_loggeduser"] = atleta.id

            return redirect ("/showcards")
        else:
            return render_template("log-in.html", loginError = True)
    
    except:
        # notifica di errore
        # return json.dumps(atleta, default=vars)
        return redirect ('/login')


@app.route('/register', methods = ['GET'])
def getRegister():
    return render_template("sign-in.html", signinError = False)

@app.route('/register', methods = ['POST'])
def register():
    email = request.form.get('inputEmail')
    password = request.form['inputPassword']
    name = request.form['inputNome']
    surname = request.form['inputCognome']
    date_of_birth = request.form['inputDate']

    sql = "select email from athletes where email = '%s'" % (email)
    cursor.execute(sql)
    emailCheck = cursor.fetchone()
    
    if emailCheck == None:

        cursor.execute(f"""insert into athletes (email, password_, name_, surname, date_of_birth) values ('{email}', '{password}',
                    '{name}','{surname}','{date_of_birth}')""")
        
        # capire cosa serve
        cursor.connection.commit()

        session["id_loggeduser"] = cursor.lastrowid

        return redirect ("/showcards")
    
    else:
        return render_template("sign-in.html", signinError = True)
    

@app.route('/api/register', methods = ['POST'])
def apiRegister():

    email = request.form.get('inputEmail')
    password = request.form.get('inputPassword')
    name = request.form.get('inputNome')
    surname = request.form.get('inputCognome')
    date_of_birth = request.form.get('inputDate')
    
    # date_of_birth = str (date_of_birth)

    sql = "select email from athletes where email = '%s'" % (email)
    cursor.execute(sql)
    emailCheck = cursor.fetchone()
    
    if emailCheck == None:

        atleta = None

        cursor.execute(f"""insert into athletes (email, password_, name_, surname, date_of_birth) values ('{email}', '{password}',
                    '{name}','{surname}','{date_of_birth}')""")
        
        sql = "select * from athletes where email = '%s' AND password_ = '%s'" % (email,password)
        cursor.execute(sql)
        row = cursor.fetchone()

        # date_of_birth = str (date_of_birth)

        atleta = Athletes (row[0],row[1],row[2],row[3],row[4],row[5])   
        
        # atleta.date_of_birth = str (atleta.date_of_birth)

        # cursor.connection.commit()

        jsonret = json.dumps(atleta, default=vars)
        print(jsonret)
        return jsonret
    
    else:

        return jsonify ("Errore"), 203



@app.route("/account")
def getAccount():
    if session["id_loggeduser"] == None:
        return redirect("/login")
    
    id = session["id_loggeduser"]

    sql = (f"select * from athletes where athletes_id = {id}")
    cursor.execute(sql)
    row = cursor.fetchone()
    
    atleta = Athletes (row[0],row[1],row[2],row[3],row[4],row[5])

    return render_template("my_account.html", athlete = atleta)

@app.route('/account', methods = ['POST'])
def update():

    id = session["id_loggeduser"]

    email = request.form['inputEmail']
    password = request.form['inputPassword']
    name = request.form['inputNome']
    surname = request.form['inputCognome']
    date_of_birth = request.form['inputDate']


    cursor.execute(f"""update athletes
                set email = '{email}', password_ = '{password}', name_ = '{name}', surname = '{surname}', date_of_birth = '{date_of_birth}'
                where athletes_id = {id}""")


    cursor.connection.commit()

    return redirect ("/account")



# @app.route('/showcards')
# def showCard():
#     id = session["id_loggeduser"]
#     # id = 1

#     sql = """select trainingCards.trainingCards_id, trainingCards.name_table, trainingCards.date_, exercises.exercise_name,
#         cardsComposition.series, cardsComposition.reps, cardsComposition.loads,cardsComposition.rest,
#         cardsComposition.duration, trainingCards.comment_
#         from trainingCards
#         left join athletes on trainingcards.athletes_fk = athletes.athletes_id
#         inner join cardsComposition on trainingCards.trainingCards_id = cardsComposition.trainingCards_fk
#         inner join exercises on cardsComposition.exercises_fk = exercises.exercises_id
#         where athletes.athletes_id = '%s'""" % (id)
    
#     cursor.execute(sql)
#     cards = cursor.fetchall()

#     schede=[]

#     numeroschede = 0

#     for c in cards:
#         scheda = TrainingCardsWeb (c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9])
#         schede.append(scheda)
#         numeroschede = numeroschede + 1

#     return render_template("schede.html", schede = schede)


@app.route('/showcards')
def showCard():
    if session["id_loggeduser"] == None:
        return redirect("/login")

    return render_template("schede.html")


# PER SITO WEB
@app.route('/showcardsJson', methods = ['GET'])
def showCardJson():
    id = session["id_loggeduser"]
    # id = 1

    sql = """select trainingCards.trainingCards_id, trainingCards.name_table, trainingCards.date_, exercises.exercise_name,
        cardsComposition.series, cardsComposition.reps, cardsComposition.loads,cardsComposition.rest,
        cardsComposition.duration, trainingCards.comment_
        from trainingCards
        left join athletes on trainingcards.athletes_fk = athletes.athletes_id
        inner join cardsComposition on trainingCards.trainingCards_id = cardsComposition.trainingCards_fk
        inner join exercises on cardsComposition.exercises_fk = exercises.exercises_id
        where athletes.athletes_id = '%s'""" % (id)
    
    cursor.execute(sql)
    cards = cursor.fetchall()

    schede=[]

    # numeroschede = 0

    for c in cards:
        scheda = TrainingCardsWeb (c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9])
        schede.append(scheda)
        # numeroschede = numeroschede + 1

    # return {schede}
    return json.dumps(schede, default=vars)
    # return render_template("my_account.html", datiSchede = schede, nSchede = numeroschede)


@app.route('/api/<id>/showcards', methods=['GET'])
def showCardAndroidJson(id):
    #id = request.form.get('inputId')
    # id = session["id_loggeduser"]
    # id = 1
    sql = """select trainingCards.trainingCards_id, trainingCards.name_table, trainingCards.date_
        from trainingCards
        left join athletes on trainingcards.athletes_fk = athletes.athletes_id
        where athletes.athletes_id = '%s'""" % (id)
    
    cursor.execute(sql)
    cards = cursor.fetchall()

    schede=[]

    # numeroschede = 0

    for c in cards:
        scheda = TrainingCardsAndroid (c[0],c[1],c[2])
        schede.append(scheda)
        # numeroschede = numeroschede + 1

    return json.dumps(schede, default=vars)


@app.route('/api/<id>/showexercises', methods=['GET'])
def showExercisesAndroidJson(id):
    # serve id scheda

    # id = 1

    sql = """select trainingCards.trainingCards_id, exercises.exercise_name, trainingCards.date_, cardsComposition.series, cardsComposition.reps, cardsComposition.loads,
            cardsComposition.rest, cardsComposition.duration, trainingCards.comment_
            from exercises
	        inner join cardsComposition on cardsComposition.exercises_fk = exercises.exercises_id
	        inner join trainingCards on cardsComposition.trainingCards_fk  = trainingCards.trainingCards_id
            where trainingCards.trainingCards_id = '%s'""" % (id)
    
    cursor.execute(sql)
    elementi = cursor.fetchall()

    righe=[]

    for c in elementi:
        riga = CardsComposition (c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8])
        righe.append(riga)

    return json.dumps(righe, default=vars)


@app.route('/api/<id>/createcard', methods=['GET'])
def createCard(id):

    athlete_id = request.form.get('inputAthleteId')
    trainingcard_id = request.form.get('inputTrainingCardId')
    name_table = request.form.get('inputNameTable')
    date = request.form.get('inputDate')

    cursor.execute()

    

    comment = request.form.get('inputComment')

    exercise_name = request.form.get('inputExercise')

    sql = "select exercises_id from exercises where exercise_name = '%s'" % (exercise_name)
    cursor.execute(sql)
    exercise_id = cursor.fetchone()

    series = request.form.get('inputSeries')
    reps = request.form.get('inputReps')
    loads = request.form.get('inputLoads')
    rest = request.form.get('inputRest')
    duration = request.form.get('inputDuration')
    

    # serve id scheda

    # id = 1

    cursor.execute(f"""insert into triningCards (athletes_fk, name_table, date_, comment_)
                    values ('{athlete_id}','{name_table}','{date}','{comment}');
                    insert into cardsComposition (trainingCards_fk, exercises_fk, series, reps, loads, rest, duration)
                    values ('{trainingcard_id}', '{exercise_id}', '{series}','{reps}','{loads}','{rest}','{duration}')""")
        

    # righe=[]

    # for c in elementi:
    #     riga = CardsComposition (c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8])
    #     righe.append(riga)

    return jsonify ("Successo")
    


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

'''
@app.route('/cardsComposition', methods = ['GET'])
def showCardComposition():
    
    id = request.args.get('trainingCards_id')
    sql = """select exercises.exercise_name, trainingCards.date_, cardsComposition.series, cardsComposition.reps,
                cardsComposition.loads, cardsComposition.rest, cardsComposition.duration, trainingCards.comment_
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

    # print(allenamentiGiornata)

    return json.dumps(allenamentiGiornata, default=vars)
'''

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



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
