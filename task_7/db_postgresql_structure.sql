-- Создание БД
CREATE DATABASE university;

\c university

CREATE TABLE student_group(
    id serial,
    group_number integer NOT NULL,
    faculty text NOT NULL,
    UNIQUE (group_number, faculty),
    PRIMARY KEY ( id )
);

CREATE TABLE birthplace(
    address text NOT NULL,
    PRIMARY KEY ( address )
);

CREATE TABLE student(
    id serial,
    surname     text NOT NULL,
    name        text NOT NULL,
    middle_name text NOT NULL,
    birthdate   date NOT NULL,
    birthplace_id   text NOT NULL,
    group_id    integer NOT NULL,
    is_studying boolean NOT NULL,

    UNIQUE (surname, name, middle_name, birthdate, birthplace_id),
    FOREIGN KEY ( birthplace_id )
        REFERENCES birthplace ( address ),
    FOREIGN KEY ( group_id )
        REFERENCES student_group ( id )
);

-- Создание записей в таблицах
INSERT INTO student_group (group_number, faculty)
    VALUES  (100, 'А'),
            (101, 'Б'),
            (102, 'В'),
            (103, 'Г');

INSERT INTO birthplace (address)
    VALUES  ('Уфа'),
            ('Москва'),
            ('Нью Йорк'),
            ('Лондон');

INSERT INTO student (surname, name, middle_name, birthdate, birthplace_id, group_id, is_studying)
    VALUES  ('Иванов', 'Иван', 'Иванович', '1990-01-01', 'Уфа', 1, TRUE),
            ('Сидоров', 'Сидр', 'Сидорович', '1991-01-01', 'Москва', 2, TRUE),
            ('Осипов', 'Вальфред', 'Максимович', '1990-01-19', 'Лондон', 1, FALSE),
            ('Орловская', 'Софо', 'Филипповна', '1990-07-07', 'Нью Йорк', 3, TRUE),
            ('Яндутова', 'Райша', 'Игоревна', '1992-06-16', 'Уфа', 3, TRUE),
            ('Брежнев', 'Лаис', 'Кириллович', '1989-12-02', 'Нью Йорк', 2, FALSE),
            ('Дружинин', 'Гимад', 'Тимофеевич', '1991-04-14', 'Москва', 3, TRUE);

-- Примеры запросов
-- Получить спиоск всех студентов
SELECT * FROM student;

-- Получить группы, где не было ни одного студента
SELECT * FROM student_group WHERE id not in (select distinct group_id from student);

-- Получить все места рождения, где студенты до сих пор учатся
SELECT * FROM birthplace WHERE address in (select distinct birthplace_id from student where is_studying);

-- Вывести Фамилию, Имя студента и их факультеты, которые учатся
SELECT s.surname, s.name, g.faculty
FROM student AS s
JOIN student_group AS g on g.id=s.group_id
where is_studying;

-- Вывести группу и факультет, где количество студентов за всё время было больше двух
SELECT *
FROM student_group
WHERE id in (
    SELECT group_id
    FROM student
    GROUP BY group_id
    HAVING count(*)>2
);

-- Вывести все факультеты и количество всех обучающихся в этих факультетах в настоящий момент
WITH t as (
    SELECT group_id, count(*) as count_student
    FROM student
    GROUP BY group_id)
SELECT g.faculty, COALESCE(sum(t.count_student), 0) AS count_student
FROM student_group as g
LEFT JOIN t on t.group_id=g.id
GROUP BY faculty
ORDER BY count_student DESC;
