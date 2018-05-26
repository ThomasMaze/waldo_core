DROP TABLE IF EXISTS bottle;

CREATE TABLE bottle (
    id INT PRIMARY KEY  NOT NULL,
    name VARCHAR(50)    NOT NULL,
    vintage INT         NOT NULL,
    type    VARCHAR(10) NOT NULL,
    price FLOAT         NOT NULL
);

