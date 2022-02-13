USE dojos_ninjas_schema;

select * from  dojos;

select * from ninjas;

UPDATE dojos SET name = 'snakes_dojo' WHERE id = 4;
UPDATE dojos SET name = 'grasshopper_dojo' WHERE id = 5;
UPDATE dojos SET name = 'cheetah_dojo' WHERE id = 6;

DELETE FROM dojos WHERE id=7;

SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id=ninjas.dojo_id;

