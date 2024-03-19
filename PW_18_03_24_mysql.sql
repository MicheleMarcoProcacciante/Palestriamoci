drop database if exists PalestriamociDB;

create database PalestriamociDB;
use PalestriamociDB;



create table athletes(
 athletes_id int primary key auto_increment,
 password_ varchar(50) not null,
 name_ varchar (255) not null,
 surname varchar (255) not null,
 email varchar (100) unique not null,
 date_of_birth date not null
)engine InnoDB;

create table trainingCards(
trainingCards_id int primary key auto_increment,
athletes_fk int,
constraint fk_trainingCards_athletes
foreign key (athletes_fk)
references athletes(athletes_id),
name_table varchar (100) not null,
date_ date not null
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
duration varchar(50) not null,
comment_ varchar (255)
);


insert into athletes (password_, name_, surname, email, date_of_birth)
values
	("password1", "nome1", "cognome1", "ciao@ciao.it", "20230422"),
	("password2", "nome2", "cognome2", "ciao2@ciao.it", "20230422"),
  	("password3", "nome3", "cognome3", "ciao3@ciao.it", "20230422");


insert into trainingCards (athletes_fk, name_table, date_)
values
	(1,"nomeTablla1", "20230405"),
	(1,"nomeTablla2", "20240403"),
	(1,"nomeTablla3", "20220422"),
   	(2,"nomeTablla4", "20231022"),
        (2,"nomeTablla5", "20230720"),
	(3,"nomeTablla6", "20230412");

insert into exercises (exercise_name, muscle_group, type_of_exercise,isAerobic)
values
	("ex1","quadricipite", "squat",0),
	("ex2","quadricipite", "flessioni",1),
	("ex3","quadricipite", "stacco",0),
   	("ex4","quadricipite", "panca",0),
        ("ex5","quadricipite", "affondi",1);

insert into cardsComposition (trainingCards_fk, exercises_fk, series, reps, loads, rest, duration,comment_)
values
   	(1, 2,"5","3","90kg", "2minuti","/","ciao"),
 	(2, 2, "4","10","50kg","3minuti","5","ciao2"),
 	(3, 3, "3","5","30kg","20 minuti","3","ciao3"),
 	(4, 2, "4","10","50kg","3minuti","5","ciao4"),
 	(5, 3, "3","5","30kg","20 minuti","3","ciao5");

/*query per ottenere tutte le cards di un singolo utente
(endpoint allenamenti svolti)*/

select name_table,date_
from trainingCards
where athletes_fk = 2;


/*query per trovare la data di una scheda e tutti gli esercizi fatti, dato l'id di una singola scheda
(endpoint visualizzazione_scheda)*/

select exercises.exercise_name, trainingCards.date_, cardsComposition.series, cardsComposition.reps, cardsComposition.loads,
cardsComposition.rest, cardsComposition.duration, cardsComposition.comment_
from exercises
	inner join cardsComposition on cardsComposition.exercises_fk = exercises.exercises_id
	inner join trainingCards on cardsComposition.trainingCards_fk  = trainingCards.trainingCards_id
where trainingCards.trainingCards_id = 1;


/*query per controllare se l'email di registrazione è già esistente
(endpoint registrazione)*/

select email
from athletes;
