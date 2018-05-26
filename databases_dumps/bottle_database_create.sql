DROP TABLE IF EXISTS bottle;
DROP TABLE IF EXISTS currentId;

CREATE TABLE bottle (
    id INT PRIMARY KEY  NOT NULL,
    name VARCHAR(50)    NOT NULL,
    vintage INT         NOT NULL,
    type    VARCHAR(10) NOT NULL,
    price FLOAT         NOT NULL
);

CREATE TABLE currentId (
    id INT PRIMARY KEY NOT NULL,
    cnt INT            NOT NULL
);

INSERT INTO currentId (id, cnt) VALUES (1,1);