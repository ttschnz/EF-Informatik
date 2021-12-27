-- DROP DATABASE test;

CREATE DATABASE test;
-- \c test
BEGIN TRANSACTION;
\c test
CREATE TABLE person(
    id SERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    gender VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    country_of_birth VARCHAR(50) NOT NULL
);

CREATE TABLE cars(
    brand varchar(10),
    color varchar(10),
    owner integer,
    FOREIGN KEY (owner) REFERENCES person(id));
COMMIT;

BEGIN TRANSACTION;
\c test
INSERT INTO person (first_name, last_name, email, gender, date_of_birth, country_of_birth) 
VALUES
('Teddy', 'Bear', NULL, 'female', '1980-12-25', 'China'),
('Panda', 'Bear', NULL, 'male',   '2021-11-20', 'China');

INSERT INTO cars (owner, brand)
VALUES
(1, 'Mercedes'),
(1, 'Audi'),
(2, 'Volkswagen');
COMMIT;

SELECT DISTINCT * FROM cars, person WHERE person.id = cars.owner;