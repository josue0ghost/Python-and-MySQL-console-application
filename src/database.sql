CREATE DATABASE IF NOT EXISTS pythonDB;

USE pythonDB;

CREATE TABLE users(
    id          int(25) auto_increment NOT NULL,
    name        varchar(100),
    lastname    varchar(100),
    email       varchar(100) not null,
    password    varchar(100) not null,
    created_at  date not null,

    CONSTRAINT pk_users PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
) ENGINE=InnoDb;

CREATE TABLE grades(
    id          int(25) auto_increment NOT NULL,
    user_id     int(25) not null,
    title       varchar(100) not null,
    description MEDIUMTEXT,
    created_at  date not null,
    
    CONSTRAINT pk_grades PRIMARY KEY(id),
    CONSTRAINT fk_grades_users FOREIGN KEY (user_id) REFERENCES users(id)
) ENGINE=InnoDb;