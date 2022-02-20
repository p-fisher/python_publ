USE login_regis_schema;

INSERT INTO user (f_name, l_name, pass, email, created_at) VALUES ('John','Doe','password123','jdoe@generic.mail', NOW());

SELECT * from user;

ALTER TABLE user RENAME COLUMN pass TO pwd;

INSERT INTO user (f_name,l_name,email,pwd,created_at) VALUES ('Dimwit', 'Daniels', 'ddan@duh.duh', 'pwd123', NOW());

DELETE FROM user WHERE id=4;

SELECT * FROM user WHERE email = 'berbo@email.emails'; 

SELECT * FROM user ORDER BY id DESC LIMIT 5;