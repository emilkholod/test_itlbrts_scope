CREATE DATABASE university;

\c university

CREATE TABLE student_group(
    group_number integer NOT NULL,
    faculty text NOT NULL,
    PRIMARY KEY ( group_number )
);

CREATE TABLE birthplace(
    address text NOT NULL,
    PRIMARY KEY ( address )
);

CREATE TABLE student(
    surname     text NOT NULL,
    name        text NOT NULL,
    middle_name text NOT NULL,
    birthdate   timestamptz NOT NULL,
    birthplace_id   text NOT NULL,
    group_id    integer NOT NULL,
    is_studying boolean NOT NULL,

    FOREIGN KEY ( birthplace_id )
        REFERENCES birthplace ( address ),
    FOREIGN KEY ( group_id )
        REFERENCES student_group ( group_number )
);
