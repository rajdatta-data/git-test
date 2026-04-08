use db;
CREATE TABLE customers (
    customer_id BIGINT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    address_id BIGINT
);
INSERT INTO customers (customer_id, first_name, last_name, address_id) VALUES
(1, 'Mary',   'Smith',   5),
(3, 'Linda',  'Williams',7),
(4, 'Barbara','Jones',   8),
(2, 'Madan',  'Mohan',   6);

CREATE TABLE payments (
    customer_id BIGINT PRIMARY KEY,
    amount BIGINT,
    mode VARCHAR(50),
    payment_date DATE
);
INSERT INTO payments (customer_id, amount, mode, payment_date) VALUES
(1,  60,  'Cash',           '2020-09-24'),
(2,  30,  'Credit Card',    '2020-04-27'),
(8,  110, 'Cash',           '2021-01-26'),
(10, 70,  'Mobile Payment', '2021-02-28'),
(11, 80,  'Cash',           '2021-03-01');

select *
from customers as c
inner join payments as p
on c.customer_id=p.customer_id;

select * 
from customers as C
left join payments as P
on C.customer_id=P.customer_id;

select * 
from customers as C
right join payments as P
on C.customer_id=P.customer_id;

SELECT *
FROM customers C
LEFT JOIN payments P
ON C.customer_id = P.customer_id

UNION

SELECT *
FROM customers C
RIGHT JOIN payments P
ON C.customer_id = P.customer_id;





