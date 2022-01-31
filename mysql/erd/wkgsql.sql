USE friendships_schema;

SELECT * FROM users;

INSERT INTO users (created_at, updated_at, first_name, last_name)
VALUES (NOW(), NOW(), "Alfie", "Schmidt"),
(NOW(), NOW(), "George", "Cornwall"),
(NOW(), NOW(), "Bertrand", "Gillespie"),
(NOW(), NOW(), "Fonce", "Smithers"),
(NOW(), NOW(), "Harold", "Chadwick"),
(NOW(), NOW(), "Betsy", "Klein");

SELECT * FROM friendships;

SELECT * from users;

INSERT INTO friendships (user_id, friend_id)
VALUES (1,2),(1,4),(1,6);

UPDATE friendships SET
updated_at = '2022-01-29 08:46:01'
WHERE id IN (1,2,3);

INSERT INTO friendships (user_id, friend_id, updated_at)
VALUES (2,1, NOW()),(2,3, NOW()),(2,5,NOW());

INSERT INTO friendships (user_id, friend_id, updated_at)
VALUES (3,2, NOW()),(3,5, NOW());

INSERT INTO friendships (user_id, friend_id, updated_at)
VALUES (4,3, NOW()),(5,1, NOW()),(5,6, NOW()),(6,2,NOW()),(6,3,NOW());

SELECT * FROM users 
JOIN friendships ON users.id = friendships.friend_id 
LEFT JOIN users as user2 ON friendships.user_id = users.id;

SELECT first_name,last_name,friend_id FROM users
JOIN friendships f ON f.user_id = users.id 
WHERE friend_id = 1;

SELECT COUNT(*) AS NumFriendships FROM friendships;

SELECT users.first_name, users.last_name, COUNT(user_id) as FriendsCt from friendships
JOIN users ON users.id = friendships.user_id
GROUP BY user_id
ORDER BY FriendsCt DESC;

SELECT last_name,first_name,friend_id FROM users
JOIN friendships f ON f.user_id = users.id 
WHERE friend_id = 3
ORDER BY last_name ASC;





