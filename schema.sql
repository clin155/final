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
CREATE TABLE companies(
    id INTEGER,
    name VARCHAR(40),
    country VARCHAR(40),
    PRIMARY KEY (id)
);

CREATE TABLE company_to_movie(
    company_id INTEGER,
    movie_id INTEGER,
    PRIMARY KEY (company_id, movie_id)
    FOREIGN KEY (movie_id) REFERENCES movies(id)
    FOREIGN KEY (company_id) REFERENCES companies(id)
);