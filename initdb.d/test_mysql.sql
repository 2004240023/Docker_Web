DROP DATABASE IF EXISTS test_mysql;
CREATE DATABASE test_mysql;
USE test_mysql;

DROP TABLE IF EXISTS person;
CREATE TABLE person 
(
    id INT NOT NULL PRIMARY KEY
    , name VARCHAR(100) NOT NULL
    , size DOUBLE
);

DROP TABLE IF EXISTS human;
CREATE TABLE human 
(
    id INT NOT NULL PRIMARY KEY
    , name VARCHAR(100) NOT NULL
    , height DOUBLE
    , weight DOUBLE
);

INSERT INTO person (id, name, size) VALUES (1, 'A', 100);
INSERT INTO person (id, name, size) VALUES (2, 'B', 150);
INSERT INTO person (id, name, size) VALUES (3, 'C', 200);
INSERT INTO human (id, name, height, weight) VALUES (1, 'A', 160.0, 70.7);
INSERT INTO human (id, name, height, weight) VALUES (2, 'B', 170.2, 63.8);
INSERT INTO human (id, name, height, weight) VALUES (3, 'C', 188.5, 108.9);
