CREATE TABLE IF NOT EXISTS movies(
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

CREATE TABLE IF NOT EXISTS genres(
    id INTEGER,
    name VARCHAR(40),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS pokemon(
    id INTEGER PRIMARY KEY,
    name VARCHAR(40),
    height INTEGER,
    weight INTEGER,
    type_id VARCHAR(20),
    attack INTEGER,
    defense INTEGER,
    speed INTEGER,
    FOREIGN KEY (type_id) REFERENCES type(type_id)
);

CREATE TABLE IF NOT EXISTS type(
    id INTEGER PRIMARY KEY,
    type VARCHAR(20)
);



CREATE TABLE IF NOT EXISTS dogs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(40),
    energy INTEGER,
    barking INTEGER,
    weight REAL,
    height REAL
);