-- mysql-init/init.sql

CREATE SCHEMA IF NOT EXISTS `sample`;

CREATE TABLE `sample`.`chatbot_conversations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `reference_id` VARCHAR(45) NULL,
  `timestamp` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

CREATE TABLE `sample`.`chatbot_messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `timestamp` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `reference_id` VARCHAR(45) NULL,
  `conversation_id` VARCHAR(45) NULL,
  `username` VARCHAR(150) NULL,
  `message_body` VARCHAR(2000) NULL DEFAULT NULL,
  `ai_response` VARCHAR(2000) NULL DEFAULT NULL,
  `keywords` VARCHAR(2000) NULL DEFAULT NULL,
  `data_points` VARCHAR(2000) NULL DEFAULT NULL,
  `summarized_data_points` VARCHAR(2000) NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `sample`.`chatbot_users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(150) NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `sample`.`customer_data` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(150) NULL,
  `phone_number` VARCHAR(150) NULL,
  `address` VARCHAR(150) NULL,
  `city` VARCHAR(150) NULL,
  `state` VARCHAR(150) NULL,
  `zip_code` VARCHAR(150) NULL,
  `customer_since` VARCHAR(150) NULL,
  `last_purchase` VARCHAR(150) NULL,
  PRIMARY KEY (`id`)
);

-- Insert default data
INSERT INTO `sample`.`chatbot_users` (`id`, `username`) VALUES (1, 'Jane Doe');
UPDATE `sample`.`chatbot_users` SET `username` = 'janedoe' WHERE (`id` = 1);

INSERT INTO sample.customer_data (first_name, last_name, email, phone_number, address, city, state, zip_code, customer_since, last_purchase)
VALUES
('John', 'Doe', 'johndoe@example.com', '312-555-1234', '123 Main St', 'Chicago', 'IL', '60601', '2018-07-23', '2023-09-15'),
('Emily', 'Smith', 'emilysmith@example.com', '773-555-9876', '456 Oak Ave', 'Evanston', 'IL', '60201', '2020-01-12', '2024-02-20'),
('Michael', 'Brown', 'michaelbrown@example.com', '847-555-4567', '789 Maple Rd', 'Naperville', 'IL', '60563', '2019-11-30', '2024-03-10'),
('Sarah', 'Johnson', 'sarahjohnson@example.com', '630-555-7890', '321 Pine Blvd', 'Aurora', 'IL', '60505', '2021-05-08', '2024-01-28'),
('David', 'Wilson', 'davidwilson@example.com', '312-555-6543', '654 Birch Ln', 'Schaumburg', 'IL', '60193', '2022-09-14', '2023-12-05');

-- Alter columns for chatbot_messages table
ALTER TABLE `sample`.`chatbot_messages` 
CHANGE COLUMN `message_body` `message_body` VARCHAR(2000) NULL DEFAULT NULL,
CHANGE COLUMN `ai_response` `ai_response` VARCHAR(2000) NULL DEFAULT NULL,
CHANGE COLUMN `keywords` `keywords` VARCHAR(2000) NULL DEFAULT NULL,
CHANGE COLUMN `data_points` `data_points` VARCHAR(2000) NULL DEFAULT NULL,
CHANGE COLUMN `summarized_data_points` `summarized_data_points` VARCHAR(2000) NULL DEFAULT NULL;
