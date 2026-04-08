use db;
-- Create table department
CREATE TABLE department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

INSERT INTO department (dept_id, dept_name) VALUES
(1, 'HR'),
(2, 'Finance'),
(3, 'Engineering'),
(4, 'Sales'),
(5, 'Marketing');

-- Create employees table
CREATE TABLE employees (
    EMP_ID INT PRIMARY KEY,
    NAME VARCHAR(50),
    SALARY DECIMAL(10, 2),
    MANAGER_ID INT,
    DEPARTMENT_ID INT
);

-- Insert data into employees
INSERT INTO employees (EMP_ID, NAME, SALARY, MANAGER_ID, DEPARTMENT_ID) VALUES
(1, 'Alice', 8000, NULL, 1),
(2, 'Bob', 7500, 1, 2),
(3, 'Charlie', 7200, 1, 3),
(4, 'David', 9000, 2, 2),
(5, 'Emma', 8500, 2, 3),
(6, 'Frank', 9000, NULL, 1),
(7, 'Grace', 7000, 3, 3),
(8, 'Henry', 6900, 3, 3),
(9, 'Irene', 7300, 2, 2),
(10, 'Jack', 7100, NULL, 3),
(11, 'Kathy', 8700, 4, 1),
(12, 'Liam', 6400, 5, 1),
(13, 'Mona', 7900, 6, 2),
(14, 'Nina', 8100, 6, 3),
(15, 'Oscar', 7600, 4, 2),
(16, 'Peter', 7800, 5, 1),
(17, 'Quinn', 6950, 7, 3),
(18, 'Rachel', 8450, 4, 3),
(19, 'Steve', 7700, 8, 2),
(20, 'Tina', 9100, NULL, 1);


-- ====================================================================================================================================
-- 1.	Find the employees who have the highest salary. 
SELECT Name, Salary
FROM employees
WHERE Salary = (SELECT MAX(Salary) FROM employees);

-- 2.	List all employees who work in the department with the lowest salary.
SELECT NAME , Salary, Department_ID
FROM employees
WHERE Department_ID = (SELECT department_Id
FROM employees
WHERE Salary = (SELECT MIN(SALARY) FROM employees));

-- 3.	Find the employee(s) who has/have the same salary as the employee with the highest salary.

-- 4.	List employees who do not have a manager.

-- 5.	Find the departments with more than 5 employees.

-- 6.	Find all employees who work in the same department as 'Grace'.

-- 7.	Find employees who earn more than any employee in department 3.

-- 8.	Find employees whose salary is less than the highest salary in department 2.

-- 9.	Find employees who have a salary greater than the employee with the second highest salary.

 