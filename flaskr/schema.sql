DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;


CREATE TABLE Users(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
);

CREATE TABLE Post (

ID INTEGER PRIMARY KEY AUTOINCREMENT,
autor_ID INTEGER NOT NULL,
title TEXT NOT NULL,
body TEXT NOT NULL,
FOREIGN KEY (Autor_ID) REFERENCES Users(ID)

)