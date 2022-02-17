USE email_validn_schema;

INSERT INTO emails (email, created_at) VALUES ('marie.osmond@singers.yow',NOW());

SELECT * FROM emails;

DELETE FROM emails WHERE id = 7;