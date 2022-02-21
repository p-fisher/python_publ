USE recipes_users_schema;

SELECT * FROM users;

SELECT * FROM recipes;

INSERT INTO recipes (r_name,r_info,instructions,under30,last_made,created_at,user_id) VALUES ('wet bread','a delightful combination of water and bread!','tajke a slice of white bread, dunk in water, slap onto a plate, and enjoy! garnish sparingly with corn niblets',1,'2022-02-02', NOW(), '1');

ALTER TABLE recipes RENAME COLUMN description TO r_info;

UPDATE recipes SET instructions = 'take a slice of white bread, dunk in water, slap onto a plate, and enjoy! garnish sparingly with corn niblets' WHERE id = 1;

ALTER TABLE recipes change under30 under30 varchar(3);

UPDATE recipes SET under30 = 'Yes' WHERE id = 1;

