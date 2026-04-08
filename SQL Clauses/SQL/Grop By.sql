use db;
-- 6. Find the total number of products available in each Category.
SELECT Category, count(ProductName) from product group by category;
-- 7. Calculate the average price of products grouped by Manufacturer.
select manufacturer,avg(price) from product group by manufacturer;
-- 8. Show the sum of Quantity InStock for each Category.
select category,sum(QuantityInStock) from product group by category;
-- 9. Count how many different products each Manufacturer supplies.
select manufacturer, count(productname) as Total_product from product group by manufacturer;
-- 10. Find the maximum price product in each Category.
select category,max(price) from product group by category;
