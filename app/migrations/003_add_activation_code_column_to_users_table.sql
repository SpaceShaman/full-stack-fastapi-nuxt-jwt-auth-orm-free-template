--UP
ALTER TABLE users
ADD COLUMN activation_code VARCHAR(255);
--DOWN
ALTER TABLE users
DROP COLUMN activation_code;
