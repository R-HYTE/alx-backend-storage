-- Create users table
-- Make an attribute unique directly in the table schema
-- will enforced your business rules and avoid bugs in your application
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
