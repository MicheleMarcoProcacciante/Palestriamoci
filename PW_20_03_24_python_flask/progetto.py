# successivamente da importare tutte le classi utilizzate

from athletes import Athletes
from trainingCards import TrainingCards
from flask import Flask, request
import pymysql
import json

app = Flask(__name__)

connection = pymysql.connect(host="localhost", user="root", password="306090", database="palestriamocidb", port=3306, autocommit=True)

cursor = connection.cursor()

# POST probabilmente è meglio per evitare di avere dati sull'url. capire come farlo.
@app.route('/login', methods = ['GET'])
def login():
    id = request.args.get('athletes_id')
    email = request.args.get('email')
    password = request.args.get('password_')

    try:
        cursor.execute("select athletes_id,email,password_ from athletes where email = %s AND password = %s", (email,password))
        risultato = cursor.fetchall()
        # chiedere potenziali alternative migliori al fetchall
        atleti = []

        for row in risultato:

            id = row[0]
            password = row[1]
            email = row[2]

            atleta = Athletes (id,password,email)
            atleti.append(atleta)

    except:
        # notifica di errore
        print ("Account non trovato")
    return json.dumps(risultato)



# da controllare questo endpoint
@app.route('/cardsComposition', methods = ['GET'])
def showCardComposition():

    id = request.args.get('athletes_id')
    cursor.execute("select exercises.exercise_name, trainingCards.date_, cardsComposition.series, cardsComposition.reps," +
                    "cardsComposition.loads,cardsComposition.rest, cardsComposition.duration, cardsComposition.comment_" +
                    "from exercises inner join cardsComposition on cardsComposition.exercises_fk = exercises.exercises_id" +
                    "inner join trainingCards on cardsComposition.trainingCards_fk  = trainingCards.trainingCards_id" +
                    "where trainingCards.trainingCards_id = '%s'" % (id))
    programms = cursor.fetchall()

    dayprogramms =[]


    for programm in programms:
        dayprogramm = TrainingCards (programm[0],programm[1],programm[2],programm[3],programm[4],programm[5],programm[6],programm[7],)
        dayprogramms.append(dayprogramm)

    print(dayprogramm)
    return json.dumps(dayprogramm, default=vars)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)



#endpoint visualizzazione nome scheda con data per id
    
@app.route('/Showcard')
def showCard():

    id = request.args.get('athletes_id')


    cursor.execute("select * from TrainingCards where athletes_fk = '%s'" % (id))
    cards = cursor.fetchall()

    schede=[]

    for card in cards:
        scheda = TrainingCards (card[0],card[1],card[2],card[3])
        schede.append(scheda)

    print(schede)
    return json.dumps(schede, default=vars)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    

