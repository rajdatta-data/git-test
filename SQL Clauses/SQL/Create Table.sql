create database db;
-- ================================================================================================================ 
use db;
-- ================================================================================================================
-- MYSQL Constraints  
create table product(
   ProductID int primary key,
   ProductName varchar(100) not null,
   Category varchar(50),
   QuantityInStock Int,
   Price decimal(10,2),
   Manufacturer varchar(150),
   CreatedDate date default '2025-11-18'   --  Date should be in always in single quotes
   );
-- ==================================================================================================================
insert into product(ProductID,ProductName,Category,QuantityInStock,Price,Manufacturer)values
(1,'Wireless Mouse','Electronics',150,599.99,'LogiTech'),
(2,'Bluetooth Speaker','Electronics',80,1299.50,'Sony'),
(3,'Running Shoes','Footwear',60,3499.00,'Nike'),
(4,'T-shirt','Clothing',200,499.00,'Puma'),
(5,'Washing Machine','Appliances',20,2399.99,'Samsung'),
(6,'Smartphone','Electronics',100,18999.00,'Realme'),
(7,'Bagpack','Accessories',75,1199.00,'Wildcraft'),
(8,'LED Bulb Pack','Home Essentials',300,299.00,'Philips'),
(9,'Keyboard','Electronics',95,999.00,'HP'),
(10,'Water Bottle','Kitchenware',180,249.00,'Milton'),
(11,'Watch','Accessories',40,2099.00,'Fastrack'),
(12,'Laptop stand','Office supplies',50,1499.00,'Zebronics'),
(13,'Hair Dryer','Personal care',25,1799.00,'Panasonic'),
(14,'Microwave','Appliances',15,10999.00,'IFB'),
(15,'Jeans','Clothing',90,1599,'Levis');

insert into product values(16,'shirt','Clothing',50,1499.00,'Levis','2025-11-18');
insert into product values(17,'Laptop','Electronics',100,100000.00,'Dell','2025-11-18');
-- =============================================================================================================================== 
select * from product;
-- ===============================================================================================================================
-- 1.	Insert a new product — “Gaming Headset” under category “Electronics” with quantity 70, price 2999.00, manufacturer “Boat”.
insert into product values(18,'Gaming Headset','Electronics',70,299.00,'Boat','2025-11-19');
-- ==============================================================================================================================
-- 2.	Add a new product “Ceiling Fan” (category “Appliances”) with 40 in stock, price n2499.00, manufacturer “Havells”
insert into product values (19,'Ceilinng Fan','Appliances',40,2499.00,'Havells','2025-11-19');
-- ===============================================================================================================================
-- 3. Insert two new products in one query:(18, 'Table Lamp', 'Home Essentials', 60, 699.00, 'Philips') (19, 'Yoga Mat', 'Fitness', 120, 999.00, 'Decathlon')
insert into product values (20,'Table Lamp','Home Essentials',60,699.00,'Philips','2025-11-19');
insert into product values (21,'Yoga Mat','Fitnesss',120,999.00,'Decathlon','2025-11-19');
-- ===================================================================================================================================
-- 4. Update the price of “Smartphone” to 17,999.00.
update product set price=17999.00 where ProductName='Smartphone';
-- =================================================================================================================================== 
-- 5. Increase the QuantityInStock by 50 for all products in the “Clothing” category.
update product set QuantityInStock =QuantityInStock + 50 where category='Clothing';
-- ====================================================================================================================================
-- 6. Change the manufacturer of “Keyboard” to “Dell”.
update product set manufacturer="Dell" where productname='keyboard';
-- =================================================================================================================================
-- 7. Set the price of all “Electronics” products below n1000 to n1000.
UPDATE product
SET price = 1000
WHERE category = 'Electronics'
AND price < 1000;
-- ===================================================================================================================================== 
-- 8. Update the category of “Water Bottle” from “Kitchenware” to “Home Essentials”.
update product set category='Home Essentials' where productname='Water Bottle';
-- ==================================================================================================================================
-- 9. Delete the product “Wrist Watch” from the table.
delete from product where productname='Wrist Watch';
-- =====================================================================================================================================
-- 10. Remove all products where QuantityInStock is less than 25.
delete from product where quantityinstock <25;
-- =================================================================================================================================
-- 11. Delete all products belonging to the “Appliances” category.
delete from product where category='Appliances';
-- ==================================================================================================================================
-- 12. Remove the product with ProductID = 19.
delete from product where productid=19;
-- =====================================================================================================================================
-- WHERE Clause
-- 18.	Display all products that belong to the Electronics category and cost more than 1000.
select * from product where category='Electronics'and price>1000;
-- ===================================================================================================================================== 
-- 19.	Show all items whose manufacturer starts with the letter ‘S’.
select manufacturer from product where manufacturer like 's%';
-- =====================================================================================================================================
-- 20.	List all products priced between 500 and 2000.
select * from product where price between 500 and 2000;
-- =====================================================================================================================================
-- 21.	Display products where QuantityInStock is less than or equal to 50.
select * from product where quantityinstock <=50;
-- ====================================================================================================================================
-- 22.	Retrieve all products whose category is either Accessories or Footwear.
select * from product where category='Accessories' or category= 'Footwear';
-- =====================================================================================================================================
-- 23.	Show products where the manufacturer is not Sony and price is above 1000.
SELECT * FROM product WHERE manufacturer <> 'Sony' AND price > 1000;

-- ========================================================================================================================================
-- Like Operater
-- 1. Show all products whose name starts with the letter 'W'.
 select * from product where productname like 'w%'; 																																										
-- ==========================================================================================================================================  
-- 2. Display all products whose category contains the word 'Electronics'.
SELECT * from Product
WHERE Category LIKE '%Electronics%';
-- ==================================================================================================================================== 
-- 3. Retrieve products whose manufacturer name ends with the letter 's'.
select * from product
where Manufacturer LIKE '%s';
-- ============================================================================================================================ 
-- 4. Find all products whose name contains the word 'Smart'
select * from product
where productname LIKE '%Smart%';
-- =================================================================================================================================
-- 5. List all products where the manufacturer name starts with 'S'. 
select Manufacturer
from product
where manufacturer LIKE 's%';
-- =============================================================================================================================
-- Wildcard
-- 1. Show all products whose name starts with 'W' followed by any one character.
SELECT * FROM Product
WHERE Productname LIKE 'W_';
-- ===================================================================================================================================
-- 2.Display all products where the category's second letter is 'l'
select * from product
where Productname LIKE '_l';
-- =================================================================================================================
-- 3. Retrieve products whose manufacturer name starts with any letter and then 'a'.
select * from product
where manufacturer LIKE '_a%';
-- ========================================================================================================
-- 4. Find all products whose product name has 'a' as the third character.
select * from product where productname LIKE '__a%';
-- =============================================================================================
-- 5. List products whose category starts with 'A' and the second letter can be anything.
select * from product where category like 'a%';
-- =================================================================================================================================== 
-- ORDER BY Clause
-- 11. Display all products ordered by Price in descending order.
select * from product
order by price desc;
-- ==============================================================================================================================
-- 12. List products sorted by QuantityInStock in ascending order.
select * from product 
order by quantityinstock asc;
-- =======================================================================================================================
-- 13. Show products in the Appliances category sorted by Price descending.
select category from product order by price desc;
-- =============================================================================================== 
-- 14. Retrieve all products sorted by Category first and then by Price.
select * from product order by category,price asc;
-- ================================================================================================================== 
-- 15. Show the top 5 cheapest products.
select * from product order by price asc limit 5;
-- =============================================================================================================
-- 21. Show the top 3 most expensive products.
select * from product order by price desc limit 3;
-- ================================================================================================================================
-- 22. Display the first 5 products when order by ProductName.
select productname from product order by productname asc limit 5;
-- ===============================================================================================================================
-- 23. List the 2 cheapest products in the Clothing category.
select productname from product order by price asc limit 2;
-- =====================================================================================================================================
 -- ORDER BY Clause
-- 24.	Display all products sorted by ProductName alphabetically.
select * from product order by productname asc;
-- =================================================================================================================================
-- 25.	Show all records ordered by Price in descending order.
select * from product order by price desc;
-- =================================================================================================================================
-- 26.	Display all Home Essentials sorted by QuantityInStock (highest first).
select * from product where category='Home Essentials' order by QuantityInStock desc;
-- ======================================================================================================================================
-- 27.	List all products sorted by Category (A–Z) and then by Manufacturer (Z–A)
select * from product order by category asc, manufacturer desc;

