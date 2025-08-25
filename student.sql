-- student.sql
-- SQL table for student data management

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    roll INT UNIQUE,
    marks INT
);

-- Insert sample data
INSERT INTO students (name, roll, marks)
VALUES 
('Selva', 101, 90),
('Lakshmi', 102, 85);
