# successivamente da importare tutte le classi utilizzate

from athletes import Athletes
from flask import Flask, request
import pymysql
import json

app = Flask(__name__)

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="palestriamocidb",
    port=3306,
    autocommit=True
)

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
            atleti.append(atleta.__dict__)

    except:
        # notifica di errore
        print ("Account non trovato")
    return json.dumps(risultato)



@app.route('/cardsComposition', methods = ['GET'])
def login():

    id = request.args.get('athletes_id')
    cursor.execute("select exercises.exercise_name, trainingCards.date_, cardsComposition.series, cardsComposition.reps," +
                    "cardsComposition.loads,cardsComposition.rest, cardsComposition.duration, cardsComposition.comment_" +
                    "from exercises inner join cardsComposition on cardsComposition.exercises_fk = exercises.exercises_id" +
                    "inner join trainingCards on cardsComposition.trainingCards_fk  = trainingCards.trainingCards_id" +
                    "where trainingCards.trainingCards_id = '%s'" % (id))
    risultato = cursor.fetchall()

    # iniziato da login, codice sotto va modificato



# fare endpoint per visualizzazione data/nome delle schede (se c'è tempo anche registrazione)
    
@app.route('/Showcard')
def showCard():

    id = request.args.get('athletes_id')


    cursor.execute("select * from TrainingCards where athletes_fk = '%s'" % (id))
    cards = cursor.fetchall()

    schede=[]

    for card in cards:
        scheda = TrainingCard (card[0],card[1],card[2],card[3])
        schede.append(scheda)

    return json.dumps(schede)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    

