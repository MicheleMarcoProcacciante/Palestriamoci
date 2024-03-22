from athletes import Athletes
from trainingCards import TrainingCards
from cardsComposition import CardsComposition
from flask import Flask, request
import pymysql
import json

app = Flask(__name__)

connection = pymysql.connect(host="localhost", user="root", password="root", database="palestriamocidb", port=3306, autocommit=True)

cursor = connection.cursor()

# POST probabilmente è meglio per evitare di avere dati sull'url. capire come farlo.
@app.route('/login', methods = ['GET'])
def login():
    email = request.args.get('email')
    password = request.args.get('password_')

    atleta = None

    try:
        sql = "select * from athletes where email = '%s' AND password_ = '%s'" % (email,password)
        print(sql)
        cursor.execute(sql)
        row = cursor.fetchone()

        atleta = Athletes (row[0],row[1],row[2],row[3],row[4],row[5])
        print(row, atleta)
    except:
        # notifica di errore
        print ("Account non trovato")
    return json.dumps(atleta, default=vars)



# da controllare questo endpoint e primo. data ritorna "data" come dato (forse str(data) in classe)
@app.route('/cardsComposition', methods = ['GET'])
def showCardComposition():
    
    id = request.args.get('trainingCards_id')
    sql = """select exercises.exercise_name, trainingCards.date_, cardsComposition.series, cardsComposition.reps,
                cardsComposition.loads, cardsComposition.rest, cardsComposition.duration, cardsComposition.comment_
                from exercises 
                    inner join cardsComposition on cardsComposition.exercises_fk = exercises.exercises_id
                    inner join trainingCards on cardsComposition.trainingCards_fk = trainingCards.trainingCards_id
                where trainingCards.trainingCards_id = '%s'""" % (id)

    print (sql)
    cursor.execute(sql)
    risultatoQuery = cursor.fetchall()

    allenamentiGiornata = []

    for riga in risultatoQuery:
        allenamentoGiornata = CardsComposition (riga[0],riga[1],riga[2],riga[3],riga[4],riga[5],riga[6],riga[7])
        allenamentiGiornata.append(allenamentoGiornata)

    print(allenamentiGiornata)
    return json.dumps(allenamentiGiornata, default=vars)

    
@app.route('/showcards', methods = ['GET'])
def showCard():

    id = request.args.get('athletes_id')

    sql = ("select * from TrainingCards where athletes_fk = '%s'" % (id))
    cursor.execute(sql)
    cards = cursor.fetchall()

    schede=[]

    for card in cards:
        scheda = TrainingCards (card[0],card[1],card[2],card[3])
        schede.append(scheda)

    print(schede)
    return json.dumps(schede, default=vars)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)