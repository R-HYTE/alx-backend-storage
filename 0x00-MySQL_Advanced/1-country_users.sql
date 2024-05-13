-- SQL script to create a table 'users' with specific attributes
-- Define id column: integer, never null, auto-incremented, primary key
-- Define email column: string (255 characters), never null, unique
-- Define name column: string (255 characters)
-- Define country column: enumeration of countries (US, CO, TN), never null, default is US
CREATE TABLE IF NOT EXISTS users (
	id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM ('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
