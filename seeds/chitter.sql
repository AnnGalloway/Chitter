DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    content VARCHAR(160),
    user_id INTEGER,
    added_on TIMESTAMP
);

INSERT INTO users (username, first_name, last_name, email, password) VALUES ('user1', 'fname1', 'lname1', 'email1@email.com', 'password1');
INSERT INTO users (username, first_name, last_name, email, password) VALUES ('user2', 'fname2', 'lname2', 'email2@email.com', 'password2');

INSERT INTO posts(content, user_id, added_on) VALUES ('post1', 1, '2023-12-01 12:00');
INSERT INTO posts(content, user_id, added_on) VALUES ('post2', 1, '2023-12-02 12:00');
INSERT INTO posts(content, user_id, added_on) VALUES ('post3', 2, '2023-12-03 12:00');
INSERT INTO posts(content, user_id, added_on) VALUES ('post4', 2, '2023-12-04 12:00');
INSERT INTO posts(content, user_id, added_on) VALUES ('post5', 1, '2023-12-05 12:00');
