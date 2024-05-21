CREATE DATABASE psg_client_db;
GO

USE psg_client_db;
GO


CREATE TABLE clients (
    client_id INT IDENTITY(1,1) PRIMARY KEY,
    client_number NVARCHAR(255) NOT NULL UNIQUE,
    email NVARCHAR(255) NOT NULL
);
GO

/* 

IDENTITY(1,1) is equivalent AUTO_INCREMENT in MySQL, 
used to create an auto-incrementing primary key.

NVARCHAR is used instead of VARCHAR to support Unicode characters,
which is common practice in SQL server.
*/


INSERT INTO clients (client_number, email) VALUES ('12345', 'client1@example.com');
INSERT INTO clients (client_number, email) VALUES ('67890', 'client2@example.com');
INSERT INTO clients (client_number, email) VALUES ('54321', 'client3@example.com');
INSERT INTO clients (client_number, email) VALUES ('09876', 'client4@example.com');
GO
