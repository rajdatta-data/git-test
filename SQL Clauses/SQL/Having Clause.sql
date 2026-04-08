-- 16. Show the categories having an average price greater than 5000.
select Category,avg(price) as AveragePrice from product group  by category having avg(price)>5000;
-- 17. Display categories where the total stock quantity exceeds 200.
select category,sum(QuantityInStock) as Total from product group by Category having sum(QuantityInStock)>200;
-- 18. Find manufacturers where the average product price is below 2000.
select Manufacturer,avg(price) as AVG_PRICE from product group by Manufacturer having avg(price)<2000;
-- 19. Show categories that contain at least 3 different products.
select category,count(ProductName) as Total from product group by category having count(ProductName)>3;