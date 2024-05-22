CREATE DATABASE psg_client_db;

USE psg_client_db;

CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    client_number VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL
);

-- SHOW TABLES;

-- DESC clients;

INSERT INTO clients (client_number, email) VALUES ('12345', 'client1@example.com');
INSERT INTO clients (client_number, email) VALUES ('67890', 'client2@example.com');
INSERT INTO clients (client_number, email) VALUES ('54321', 'client3@example.com');
INSERT INTO clients (client_number, email) VALUES ('09876', 'client4@example.com');

-- SELECT * FROM clients;
select * from clients;

UPDATE clients
SET 
email = "newgeeksontheblockconnect@gmail.com"
WHERE client_number = "09876";


