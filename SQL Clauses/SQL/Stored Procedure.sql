use db;
CREATE TABLE employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE
);

INSERT INTO employee (first_name, last_name, department, salary, hire_date)
VALUES
('John', 'Doe', 'IT', 55000.00, '2021-04-15'),
('Emma', 'Watson', 'HR', 48000.00, '2020-06-01'),
('Liam', 'Smith', 'Finance', 62000.00, '2019-09-23'),
('Sophia', 'Brown', 'Marketing', 51000.00, '2022-01-10'),
('William', 'Taylor', 'IT', 58000.00, '2018-07-30');

-- ==============================================================================
-- 1.	Create a stored procedure to fetch all employees hired after a specific date (use an IN parameter).













 