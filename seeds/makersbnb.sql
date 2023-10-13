-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    start_date DATE,
    end_date DATE,
    price INTEGER,
    user_id INTEGER,
    constraint fk_user_spaces foreign key(user_id) references users(id) on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    start_date DATE,
    end_date DATE,
    user_id INTEGER,
    space_id INTEGER,
    constraint fk_user_bookings foreign key(user_id) references users(id) on delete cascade,
    constraint fk_space foreign key(space_id) references spaces(id) on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (name, email, password) VALUES ('user1', 'user1@email.com', 'password1');
INSERT INTO users (name, email, password) VALUES ('user2', 'user2@email.com', 'password2');
INSERT INTO spaces (name, description, start_date, end_date, price, user_id) VALUES ('space1', 'description1', '2030-01-01', '2030-02-01', 1000, 1);
INSERT INTO spaces (name, description, start_date, end_date, price, user_id) VALUES ('space2', 'description2', '2031-02-02', '2031-02-28', 15000, 1);
INSERT INTO spaces (name, description, start_date, end_date, price, user_id) VALUES ('space3', 'description3', '2030-01-15', '2030-02-15', 2000, 2);
INSERT INTO spaces (name, description, start_date, end_date, price, user_id) VALUES ('space4', 'description4', '2030-03-04', '2030-03-14', 70000, 2);
INSERT INTO bookings (start_date, end_date, user_id, space_id) VALUES ('2030-01-17', '2030-01-19', 2, 3);
INSERT INTO bookings (start_date, end_date, user_id, space_id) VALUES ('2031-02-10', '2031-02-17', 1, 2);
INSERT INTO bookings (start_date, end_date, user_id, space_id) VALUES ('2030-03-04', '2030-03-08', 2, 4);
INSERT INTO bookings (start_date, end_date, user_id, space_id) VALUES ('2030-01-25', '2030-02-01', 1, 1);