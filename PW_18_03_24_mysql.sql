drop database if exists PalestriamociDB;

create database PalestriamociDB;
use PalestriamociDB;



create table athletes(
 id int primary key auto_increment,
 password_ varchar(50) not null,
 name_ varchar (255) not null,
 surname varchar (255) not null,
 email varchar (100) unique not null,
 date_of_birth date not null
)engine InnoDB;

create table trainigCards(
id int primary key auto_increment,
id_athletes int,
constraint fk_trainingCards_athletes
foreign key (id_athletes)
references athletes(id),
name_table varchar (100) not null,
create_date date not null
)engine InnoDB; 

create table exercises(
id int primary key auto_increment,
exercises_name varchar (50) not null,
muscle_group varchar (50) not null,
type_of_exercise varchar (10) not null
);

create table cardsComposition(
id int primary key auto_increment,
id_trainigCards int,
constraint fk_cardsComposition_trainigCards
foreign key (id_trainigCards)
references trainigCards(id),
id_exercises int,
constraint fk_cardsComposition_exercises
foreign key (id_exercises)
references exercises(id),
series varchar(50) not null,
reps varchar(50) not null,
loads varchar (50) not null,
rest varchar(50) not null,
duration varchar(50) not null,
isAerobic tinyint,
comment_ varchar (255)
);


insert into athletes (id, password_, name_, surname, email, date_of_birth)
values
	(1,"password", "nome", "cognome", "ciao@ciao.it", "20230422"),
	(2,"password", "nome", "cognome", "ciao2@ciao.it", "20230422"),
    (3,"password", "nome", "cognome", "ciao3@ciao.it", "20230422")


