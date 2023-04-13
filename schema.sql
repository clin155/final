CREATE TABLE movies(
id INTEGER,
title VARCHAR(40),
genre_id INTEGER,
popularity INTEGER,
rating INTEGER,
release_date VARCHAR(40),
revenue INTEGER,
FOREIGN KEY (genre_id) REFERENCES genres(id)
PRIMARY KEY (id)
);

CREATE TABLE genres(
    id INTEGER,
    name VARCHAR(40),
    PRIMARY KEY (id)
);

CREATE TABLE pokemon(
    id INTEGER PRIMARY KEY,
    name VARCHAR(40),
    height INTEGER,
    weight INTEGER,
    type VARCHAR(20),
    attack INTEGER,
    defense INTEGER,
    speed INTEGER
);

CREATE TABLE dogs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(40),
    energy INTEGER,
    barking INTEGER,
    weight REAL,
    height REAL
);