use db;
-- ============================FUNCTIONS==================================================
-- 1.STRING Functions
-- UPPER()
SELECT UPPER(Name) FROM employees;
-- LOWER()
SELECT LOWER(Name) FROM employees;
-- LENGTH()
SELECT LENGTH(Name) FROM employees;
-- SUBSTRING()=Extracts part of string
-- SELECT substring(column_name,start_position,length) FROM employees;
SELECT SUBSTRING(name,1,3) FROM employees;
-- CONCAT()=Joins two or more strings
-- SELECT  CONCAT(Column1,column2,....) FROM table_name;
SELECT CONCAT(name,"_",department_ID) FROM employees;
-- REPLACE()=Replaces parts of string with another string
-- SELECT REPLACE(Column_name,'old','new') FROM table_name;
SELECT REPLACE(Name,"Bob","Amruta") from  employees;
CREATE Table em(Emp_name VARCHAR(50));
-- TRIM()=Removes spaces from the beginning and end.
-- SELECT TRIM(Column_name) FROM table_name;
-- SELECT TRIM(Emp_Name) FROM table_name;
SELECT * FROM employees;
-- 2.NUMERIC Functions
-- MATH Library
-- ABS()= Returns Absolute (Positive) Value;
SELECT ABS(column_name) FROM table_name;
SELECT ABS(-60000) FROM em ;
-- ROUND()=Rounds a number to given decimal places
SELECT ROUND(Column_name,decimal_places) FROM table_name;
SELECT ROUND(3000.45) FROM em;
-- CEIL()=Rounds number UP to next integer
SELECT CEIL(column_name) FROM Table_name;
SELECT CEIL(20.34) FROM em;
-- FLOOR()=Rounds number DOWN to the previous integer
SELECT FLOOR(Column_name) FROM Table_name;
-- MOD()=Returns remainder of division.
SELECT MOD(cloumn_name,number)FROM table_name;
-- POWER()=Raises a number to a power.
SELECT POWER(column_name,power_value) FROM table_name;

USE augsql;
-- ================================================Stored Procedure===============================================================
-- ================================================User defined function========================================================
-- Deterministic=>return same result for same input
-- Non deterministic=>Differnet result for same input ==Time
DELIMITER //
CREATE FUNCTION square1 (x INT)
RETURNS INT
DETERMINISTIC
BEGIN
	return x * x;
    
END //
DELIMITER ;
SELECT square(5);
SELECT square(55);
-- write UDF to 
DELIMITER //
CREATE FUNCTION FULL_name1(name VARCHAR(50),surname VARCHAR(50))
RETURNS VARCHAR(100)
DETERMINISTIC
BEGIN
    RETURN CONCAT(NAME ," ", surname);
END //
DELIMITER ;

SELECT FULL_name1('Amruta','pol');


DELIMITER //
CREATE FUNCTION is_even1(x INT)
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
   RETURN IF(x%2=0,"EVEN","ODD");
END //
DELIMITER ;

SELECT is_even1(9);

DELIMITER //
CREATE FUNCTION Simple_intrest(p DECIMAL(10,2), r DECIMAL(5,2),t INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    RETURN (p*r*t)/100;
END //
DELIMITER ;

SELECT Simple_intrest(1000,2,4);

DROP FUNCTION  IF EXISTS FULL_name;

-- is palindrom or not

DELIMITER //
CREATE FUNCTION is_palindrom(a VARCHAR(100))
RETURNS BOOLEAN
DETERMINISTIC
BEGIN
	RETURN a = REVERSE(a);
END //
DELIMITER ;
SELECT is_palindrom("racecar");
SELECT is_palindrom("amruta");

-- write a UDF to get age from birthdate

DELIMITER //
CREATE FUNCTION get_age(birthdate DATE)
RETURNS INT
deterministic
BEGIN
	RETURN TIMESTAMPDIFF(YEAR,birthdate,CURDATE());
END //
DELIMITER ;

SELECT get_age('2003-04-10');