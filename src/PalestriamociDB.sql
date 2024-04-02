drop database if exists PalestriamociDB;

create database PalestriamociDB;
use PalestriamociDB;



create table athletes(
 athletes_id int primary key auto_increment,
 email varchar (100) unique not null,
 password_ varchar(50) not null,
 name_ varchar (255) not null,
 surname varchar (255) not null,
 date_of_birth date not null
)engine InnoDB;

 

create table trainingCards(
trainingCards_id int primary key auto_increment,
athletes_fk int,
constraint fk_trainingCards_athletes
foreign key (athletes_fk)
references athletes(athletes_id),
name_table varchar (100) not null,
date_ date not null,
comment_ varchar (255)
)engine InnoDB; 

create table exercises(
exercises_id int primary key auto_increment,
exercise_name varchar (50) not null,
muscle_group varchar (50) not null,
type_of_exercise varchar (10) not null,
isAerobic tinyint
);

create table cardsComposition(
cardsComposition_id int primary key auto_increment,
trainingCards_fk int,
constraint fk_cardsComposition_trainingCards
foreign key (trainingCards_fk)
references trainingCards(trainingCards_id),
exercises_fk int,
constraint fk_cardsComposition_exercises
foreign key (exercises_fk)
references exercises(exercises_id),
series varchar(50) not null,
reps varchar(50) not null,
loads varchar (50) not null,
rest varchar(50) not null,
duration varchar(50) not null
);


insert into athletes (email, password_, name_, surname, date_of_birth)
values
	("ciao@ciao.it", "12345678", "nome1", "cognome1", "20230422"),
	("ciao1@ciao.it", "87654321", "nome2", "cognome2", "20230423"),
	("ciao2@ciao.it", "12345678", "nome3", "cognome3", "20230424");


insert into trainingCards (athletes_fk, name_table, date_,comment_)
values
	(1,"nomesc Aldo", "20230405", "brutto commento"),
	(1,"sc Giovanni", "20240403", "bel commento"),
	(1,"sc Giacomo", "20220422", "mi sono annoiato"),
   	(2,"Bracco", "20231022", "mi sono divertito"),
	(2,"Baldo", "20230720", "commento"),
	(3,"Geppetto", "20230412", "no comment");

insert into exercises (exercise_name, muscle_group, type_of_exercise,isAerobic)
values
	/*parlare con samuele su se eliminare type_of_exercise o isAerobic*/
    ("Affondi in camminata bilanciere", "quadricipite", 0),
    ("Affondi in camminata manubri", "quadricipite", "Affondi in camminata bilanciere", 0),
    ("Affondi retro bilanciere","quadricipite", "Affondi retro bilanciere",0),
    ("Affondi retro manubri","quadricipite", "Affondi retro manubri",0),
    ("Squat belt","quadricipite", "squat",0),
    ("Squat bulgarain bilanciere","quadricipite", "squat",0),
    ("Squat bulgarain manubri","quadricipite", "squat",0),
    ("Squat hack","quadricipite", "squat",0),
    ("Military press bilanciere","quadricipite", "squat",0),
    ("Military press bilanciere da seduto","quadricipite", "squat",0),
    ("Military press manubri","quadricipite", "squat",0),
    ("Military press manubri da seduto","quadricipite", "squat",0),
    ("Panca piana bilanciere","quadricipite", "squat",0),
    ("Panca piana manubri","quadricipite", "squat",0),
    ("Squat high bar","quadricipite", "squat",0),
    ("Squat low bar","quadricipite", "squat",0),
    ("Stacco a gambe tese","quadricipite", "squat",0),
    ("Stacco da terra","quadricipite", "squat",0),
    ("Stacco rumeno","quadricipite", "squat",0),
    ("Leg curl da seduto","quadricipite", "squat",0),
    ("Leg curl da sdraiato","quadricipite", "squat",0),
    ("Leg extension","quadricipite", "squat",0),
    ("Pectoral Machine","quadricipite", "squat",0),
    ("Chest press","quadricipite", "squat",0),
    ("Chest press incline","quadricipite", "squat",0),
    ("Shoulder press","quadricipite", "squat",0),
    ("Alzate laterali manubri","quadricipite", "squat",0),
    ("Alzate laterali ai cavi","quadricipite", "squat",0),
    ("Hip thrust bilanciere","quadricipite", "squat",0),
    ("Panca inclinata bilanciere","quadricipite", "squat",0),
    ("Panca inclinata manubri","quadricipite", "squat",0),
    ("Hip thrust machine","quadricipite", "squat",0),
    ("Row machine","quadricipite", "squat",0),
    ("Lat machine presa prona","quadricipite", "squat",0),
    ("Lat machine presa neutra","quadricipite", "squat",0),
    ("Lat machine presa supina","quadricipite", "squat",0),
    ("Pulley","quadricipite", "squat",0),
    ("Rematore bilanciere","quadricipite", "squat",0),
    ("Rematore manubri","quadricipite", "squat",0),
    ("Rematore manubri su panca inclinata","quadricipite", "squat",0),
    ("Alzate posteriori manubri su panca","quadricipite", "squat",0),
    ("Alzate posteriori ai cavi","quadricipite", "squat",0),
    ("Stacco rumeno manubri","quadricipite", "squat",0),
    ("Croci manubri panca piana","quadricipite", "squat",0),
    ("Croci manubri panca inclinata","quadricipite", "squat",0),
    ("Croci ai cavi","quadricipite", "squat",0),
    ("Curl manubri","quadricipite", "squat",0),
    ("Curl bilanciere","quadricipite", "squat",0),
    ("Curl manubri su panca inclinata","quadricipite", "squat",0),
    ("Curl spider","quadricipite", "squat",0),
    ("Curl bayesain","quadricipite", "squat",0),
    ("Push down","quadricipite", "squat",0),
    ("French press manubri","quadricipite", "squat",0),
    ("French press bilanciere","quadricipite", "squat",0),
    ("Kick back manubri","quadricipite", "squat",0),
    ("Kick back ai cavi","quadricipite", "squat",0),
    ("Pressa orizzontale","quadricipite", "squat",0),
    ("Pressa inclinata","quadricipite", "squat",0),
    ("Trazioni alla sbarra presa prona","quadricipite", "squat",0),
    ("Trazioni alla sbarra presa supina","quadricipite", "squat",0),
    ("Trazioni alla sbarra presa neutra","quadricipite", "squat",0),
    ("Dip alle parallele","quadricipite", "squat",0),
    ("Push up","quadricipite", "squat",0),
    ("Calf multipower","quadricipite", "squat",0),
    ("Calf seduto","quadricipite", "squat",0),
    ("Calf alla pressa","quadricipite", "squat",0),
    ("Panca inclinata multipower","quadricipite", "squat",0),
    ("Military press multipower","quadricipite", "squat",0),
    ("Squat split multipower","quadricipite", "squat",0),
    ("Crunch da terra","quadricipite", "squat",0),
    ("Sit up","quadricipite", "squat",0),
    ("Plank","quadricipite", "squat",0),
    ("Plank side","quadricipite", "squat",0),
    ("Iperestensioni","quadricipite", "squat",0),
    ("Tapis roulant","quadricipite", "squat",0),
    ("Cyclette","quadricipite", "squat",0),
    ("Elittica","quadricipite", "squat",0),
    ("Vogatore","quadricipite", "squat",0);

insert into cardsComposition (trainingCards_fk, exercises_fk, series, reps, loads, rest, duration)
values
   	(1, 1,"2","30","60kg", "1minuti","3minuti"),
	(1, 2,"5","42","95kg", "3minuti","/"),
	(1, 3,"8","50","300kg", "7minuti","8minuti"),
 	(2, 2, "4","10","50kg","3minuti","5minuti"),
 	(3, 3, "1","5","30kg","20minuti","3minuti"),
 	(4, 2, "10","100","5kg","3minuti","5minuti"),
 	(5, 5, "23","10","30kg","20minuti","3minuti");

/*query per ottenere tutte le cards di un singolo utente
(endpoint allenamenti svolti)*/

select name_table,date_
from trainingCards
where athletes_fk = 2;


/*query per trovare la data di una scheda e tutti gli esercizi fatti, dato l'id di una singola scheda
(endpoint visualizzazione_scheda)*/

select exercises.exercise_name, trainingCards.date_, cardsComposition.series, cardsComposition.reps, cardsComposition.loads,
cardsComposition.rest, cardsComposition.duration, trainingCards.comment_
from exercises
	inner join cardsComposition on cardsComposition.exercises_fk = exercises.exercises_id
	inner join trainingCards on cardsComposition.trainingCards_fk  = trainingCards.trainingCards_id
where trainingCards.trainingCards_id = 1;



select trainingCards.trainingCards_id, athletes.athletes_id, trainingCards.name_table, trainingCards.date_, exercises.exercise_name,
cardsComposition.series, cardsComposition.reps, cardsComposition.loads,cardsComposition.rest,
cardsComposition.duration, trainingCards.comment_
from trainingCards
    left join athletes on trainingcards.athletes_fk = athletes.athletes_id
    inner join cardsComposition on trainingCards.trainingCards_id = cardsComposition.trainingCards_fk
    inner join exercises on cardsComposition.exercises_fk = exercises.exercises_id
where athletes.athletes_id = 1;


/*query per controllare se l'email di registrazione è già esistente
(endpoint registrazione)*/

select email
from athletes;
/*select email , password_ from athletes; */
