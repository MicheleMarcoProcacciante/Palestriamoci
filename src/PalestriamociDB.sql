drop database if exists PalestriamociDB;

create database PalestriamociDB;
use PalestriamociDB;



create table athletes(
 athletes_id int primary key auto_increment,
 email varchar
(100) unique not null,
 password_ varchar
(50) not null,
 name_ varchar
(255) not null,
 surname varchar
(255) not null,
 date_of_birth date not null
)engine InnoDB;



create table trainingCards(
trainingCards_id int primary key auto_increment,
athletes_fk int,
constraint fk_trainingCards_athletes
foreign key
(athletes_fk)
references athletes
(athletes_id),
name_table varchar
(100) not null,
date_ date not null,
comment_ varchar
(255)
)engine InnoDB;

create table exercises(
exercises_id int primary key auto_increment,
exercise_name varchar
(50) not null,
isAerobic tinyint not null
);

create table cardsComposition(
cardsComposition_id int primary key auto_increment,
trainingCards_fk int,
constraint fk_cardsComposition_trainingCards
foreign key
(trainingCards_fk)
references trainingCards
(trainingCards_id),
exercises_fk int,
constraint fk_cardsComposition_exercises
foreign key
(exercises_fk)
references exercises
(exercises_id),
series int not null,
reps int not null,
loads int not null,
rest int not null,
duration int not null
);


insert into athletes
    (email, password_, name_, surname, date_of_birth)
values
    ("riccardo.falchetto@gmail.com", "12345678", "Riccardo", "Falchetto", "19950511"),
    ("mihele.procacciante@gmail.com", "12345678", "Michele" , "Procacciante", "20040501"),
    ("vittorio.longo@gmail.com", "12345678", "Vittorio", "Longo", "19930920"),
    ("samuele.filincieri@gmail.com", "12345678", "Samuele", "Filinceri", "20040917"),
    ("mykola.kartsev@gmail.com", "12345678", "Mykola", "Kartsev", "19890707"),
    ("francesco.pirollo@gmail.com", "12345678", "Francesco", "Pirollo", "20240409");


insert into trainingCards
    (athletes_fk, name_table, date_,comment_)
values
    (1, "scheda riccardo", 20240409, "commento..."),
    (1, "falchetto sheda", 20240409, "commento..."),
    (1, "sc riccardofalchetto", 20240409, "commento..."),
    (2, "scheda michele", 20240409, "commento..."),
    (2, "procacciante scheda", 20240409, "commento..."),
    (2, "sc micheleprocacciante", 20240409, "commento..."),
    (3, "scheda vittorio", 20240409, "commento..."),
    (3, "longo scheda", 20240409, "commento..."),
    (3, "sc vittoriolono", 20240409, "commento..."),
    (4, "scheda samuele", 20240409, "commento..."),
    (4, "filincieri scheda", 20240409, "commento..."),
    (4, "sc samuelefilincieri", 20240409, "commento..."),
    (5, "scheda mykola", 20240409, "commento..."),
    (5, "kartsev scheda", 20240409, "commento..."),
    (5, "sc mykolakartsev", 20240409, "commento..."),
    (6, "scheda francesco", 20240409, "commento..."),
    (6, "pirollo scheda", 20240409, "commento..."),
    (6, "sc francescopirollo", 20240409, "commento...");


insert into exercises
    (exercise_name, isAerobic)
values
    ("Affondi in camminata bilanciere", 0),
    ("Affondi in camminata manubri", 0),
    ("Affondi retro bilanciere", 0),
    ("Affondi retro manubri", 0),
    ("Squat belt", 0),
    ("Squat bulgarain bilanciere", 0),
    ("Squat bulgarain manubri", 0),
    ("Squat hack", 0),
    ("Military press bilanciere", 0),
    ("Military press bilanciere da seduto", 0),
    ("Military press manubri", 0),
    ("Military press manubri da seduto", 0),
    ("Panca piana bilanciere", 0),
    ("Panca piana manubri", 0),
    ("Squat high bar", 0),
    ("Squat low bar", 0),
    ("Stacco a gambe tese", 0),
    ("Stacco da terra", 0),
    ("Stacco rumeno", 0),
    ("Leg curl da seduto", 0),
    ("Leg curl da sdraiato", 0),
    ("Leg extension", 0),
    ("Pectoral Machine", 0),
    ("Chest press", 0),
    ("Chest press incline", 0),
    ("Shoulder press", 0),
    ("Alzate laterali manubri", 0),
    ("Alzate laterali ai cavi", 0),
    ("Hip thrust bilanciere", 0),
    ("Panca inclinata bilanciere", 0),
    ("Panca inclinata manubri", 0),
    ("Hip thrust machine", 0),
    ("Row machine", 0),
    ("Lat machine presa prona", 0),
    ("Lat machine presa neutra", 0),
    ("Lat machine presa supina", 0),
    ("Pulley", 0),
    ("Rematore bilanciere", 0),
    ("Rematore manubri", 0),
    ("Rematore manubri su panca inclinata", 0),
    ("Alzate posteriori manubri su panca", 0),
    ("Alzate posteriori ai cavi", 0),
    ("Stacco rumeno manubri", 0),
    ("Croci manubri panca piana", 0),
    ("Croci manubri panca inclinata", 0),
    ("Croci ai cavi", 0),
    ("Curl manubri", 0),
    ("Curl bilanciere", 0),
    ("Curl manubri su panca inclinata", 0),
    ("Curl spider", 0),
    ("Curl bayesain", 0),
    ("Push down", 0),
    ("French press manubri", 0),
    ("French press bilanciere", 0),
    ("Kick back manubri", 0),
    ("Kick back ai cavi", 0),
    ("Pressa orizzontale", 0),
    ("Pressa inclinata", 0),
    ("Trazioni alla sbarra presa prona", 0),
    ("Trazioni alla sbarra presa supina", 0),
    ("Trazioni alla sbarra presa neutra", 0),
    ("Dip alle parallele", 0),
    ("Push up", 0),
    ("Calf multipower", 0),
    ("Calf seduto", 0),
    ("Calf alla pressa", 0),
    ("Panca inclinata multipower", 0),
    ("Military press multipower", 0),
    ("Squat split multipower", 0),
    ("Crunch da terra", 0),
    ("Sit up", 0),
    ("Plank", 0),
    ("Plank side", 0),
    ("Iperestensioni", 0),
    ("Tapis roulant", 1),
    ("Cyclette", 1),
    ("Elittica", 1),
    ("Vogatore", 1);

insert into cardsComposition
    (trainingCards_fk, exercises_fk, series, reps, loads, rest, duration)
values
    (1 , 1 , 5 , 10 , 60 , 2 , 3),
    (1 , 2 , 10 , 20 , 90 , 4 , 8),
    (1, 3, 5 , 10 , 60 , 2, 3 ),
    (2, 4, 10 , 20 , 90 , 4 , 8 ),
    (2, 5, 5 , 10 , 60  , 2 , 3 ),
    (2, 6, 10 , 20 , 90 , 4 , 8 ),
    (3, 7, 5 , 10 , 60  , 2 , 3 ),
    (3, 8, 10 , 20 , 90 , 4 , 8 ),
    (3, 9, 5 , 10 , 60  , 2 , 3 ),
    (4, 10, 10 , 20 , 90 , 4 , 8 ),
    (4, 11, 5, 10 , 60  , 2 , 3 ),
    (4, 12, 10 , 20 , 90 , 4 , 8 ),
    (4, 13, 5 , 10 , 60  , 2 , 3 ),
    (5, 14, 10 , 20 , 90 , 4 , 8 ),
    (5, 15, 5, 10 , 60  , 2 , 3),
    (5, 16, 10 , 20 , 90 , 4 , 8 ),
    (6, 17, 5, 10 , 60  , 2 , 3 ),
    (6, 18, 10 , 20 , 90 , 4 , 8 ),
    (6, 19, 5, 10 , 60  , 2 , 3 ),
    (7 , 1 , 5 , 10 , 60 , 2 , 3),
    (7 , 2 , 10 , 20 , 90 , 4 , 8),
    (7, 3, 5 , 10 , 60 , 2, 3 ),
    (8, 4, 10 , 20 , 90 , 4 , 8 ),
    (8, 5, 5 , 10 , 60  , 2 , 3 ),
    (8, 6, 10 , 20 , 90 , 4 , 8 ),
    (9, 7, 5 , 10 , 60  , 2 , 3 ),
    (9, 8, 10 , 20 , 90 , 4 , 8 ),
    (9, 9, 5 , 10 , 60  , 2 , 3 ),
    (10, 10, 10 , 20 , 90 , 4 , 8 ),
    (10, 11, 5, 10 , 60  , 2 , 3 ),
    (10, 12, 10 , 20 , 90 , 4 , 8 ),
    (11, 13, 5 , 10 , 60  , 2 , 3 ),
    (11, 14, 10 , 20 , 90 , 4 , 8 ),
    (11, 15, 5, 10 , 60  , 2 , 3),
    (12, 16, 10 , 20 , 90 , 4 , 8 ),
    (12, 17, 5, 10 , 60  , 2 , 3 ),
    (12, 18, 10 , 20 , 90 , 4 , 8 ),
    (13, 19, 5, 10 , 60  , 2 , 3 ),
	(14, 1 , 5 , 10 , 60 , 2 , 3),
    (14, 2 , 10 , 20 , 90 , 4 , 8),
    (14, 3, 5 , 10 , 60 , 2, 3 ),
    (15, 4, 10 , 20 , 90 , 4 , 8 ),
    (15, 5, 5 , 10 , 60  , 2 , 3 ),
    (15, 6, 10 , 20 , 90 , 4 , 8 ),
    (16, 7, 5 , 10 , 60  , 2 , 3 ),
    (16, 8, 10 , 20 , 90 , 4 , 8 ),
    (16, 9, 5 , 10 , 60  , 2 , 3 ),
    (17, 10, 10 , 20 , 90 , 4 , 8 ),
    (17, 11, 5, 10 , 60  , 2 , 3 ),
    (17, 12, 10 , 20 , 90 , 4 , 8 ),
    (18, 13, 5 , 10 , 60  , 2 , 3 ),
    (18, 14, 10 , 20 , 90 , 4 , 8 ),
    (18, 15, 5, 10 , 60  , 2 , 3);

/*query per ottenere tutte le cards di un singolo utente
(endpoint allenamenti svolti)*/

select name_table, date_
from trainingCards
where athletes_fk = 5;


/*query per trovare la data di una scheda e tutti gli esercizi fatti, dato l'id di una singola scheda
(endpoint visualizzazione_scheda)*/

select exercises.exercise_name, trainingCards.date_, cardsComposition.series, cardsComposition.reps, cardsComposition.loads,
    cardsComposition.rest, cardsComposition.duration, trainingCards.comment_
from exercises
    inner join cardsComposition on cardsComposition.exercises_fk = exercises.exercises_id
    inner join trainingCards on cardsComposition.trainingCards_fk  = trainingCards.trainingCards_id
where trainingCards.trainingCards_id = 1;



select trainingCards.trainingCards_id, athletes.athletes_id, trainingCards.name_table, trainingCards.date_, exercises.exercise_name,
    cardsComposition.series, cardsComposition.reps, cardsComposition.loads, cardsComposition.rest,
    cardsComposition.duration, trainingCards.comment_
from trainingCards
    left join athletes on trainingcards.athletes_fk = athletes.athletes_id
    inner join cardsComposition on trainingCards.trainingCards_id = cardsComposition.trainingCards_fk
    inner join exercises on cardsComposition.exercises_fk = exercises.exercises_id
where athletes.athletes_id = 4;


/*query per controllare se l'email di registrazione è già esistente
(endpoint registrazione)*/

select email
from athletes;
/*select email , password_ from athletes; */



select *
from athletes;
