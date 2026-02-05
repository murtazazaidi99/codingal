CREATE TABLE IF NOT EXISTS Salesman(
salesman_id TEXT PRIMARY KEY,
name TEXT,
city TEXT,
commission REAL
);
INSERT INTO Salesman VALUES
('5001','James Hoog','New York',0.15),
('5002','Nail Knite','Paris',0.13),
('5005','Pit Alex','London',0.11),
('5006','Mc Lyon','Paris',0.14),
('5007','Paul Adam','Rome',0.13),
('5003','Lauson Hen','San Jose',0.12);

CREATE TABLE IF NOT EXISTS Customer(
cust_id TEXT PRIMARY KEY,
cust_name TEXT,
cust_city TEXT,
grade INTEGER,
salesman_id TEXT
);
INSERT INTO Customer VALUES
('3001','James Hoog','New York',150,'5001'),
('3002','Nail Knite','Paris',113,'5002'),
('3005','Pit Alex','amrica',1111,'5003'),
('3006','Mc Lyon','Paris',314,'5004'),
('3007',' Adam','Rome',413,'5005'),
('3008',' Hen','china',512,'5006')
('3009',' cook','china',NULL,'5006')

CREATE TABLE IF NOT EXISTS Orders(
ord_noid TEXT PRIMARY KEY,
purch_amt real,
ord_date Date,
customer_id TEXT,
salesman_id TEXT
);
INSERT INTO Customer VALUES
('3001','James Hoog','New York',150 ,'3001','5001'),
('3002','Nail Knite','Paris',113,'3002','5002'),
('3005','Pit Alex','amrica',1111,'3005','5003'),
('3006','Mc Lyon','Paris',314,'3006','5004'),
('3007',' Adam','Rome',413,'3007','5005'),
('3008',' Hen','china',512,'3008','5006')
/* 1. Matching customers and salesmen by city */

SELECT c.cust_name, s.name, s.city

FROM Customer c

JOIN Salesman s

ON c.city = s.city;

/* 2. Linking customers to their salesmen */

SELECT c.cust_name, s.name

FROM Customer c

JOIN Salesman s

ON c.salesman_id = s.salesman_id;

/* 3. Orders where customer city != salesman city */

SELECT o.ord_no, c.cust_name, o.customer_id, o.salesman_id

FROM Orders o

JOIN Customer c ON o.customer_id = c.customer_id

JOIN Salesman s ON o.salesman_id = s.salesman_id

WHERE c.city <> s.city;

/* 4. All orders with customer names */

SELECT o.ord_no, c.cust_name

FROM Orders o

JOIN Customer c

ON o.customer_id = c.customer_id;

/* 5. Customers with grades */

SELECT cust_name AS Customer, grade AS Grade

FROM Customer

WHERE grade IS NOT NULL;

/* 6. Customers with salesmen where commission is between 0.12 and 0.14 */

SELECT c.cust_name AS Customer,

c.city AS City,

s.name AS Salesman,

s.commission

FROM Customer c

JOIN Salesman s

ON c.salesman_id = s.salesman_id

WHERE s.commission BETWEEN 0.12 AND 0.14;

/* 7. Commission for orders where customer grade >= 200 */

SELECT o.ord_no,

c.cust_name,

s.commission AS commission_percent,

o.purch_amt * s.commission AS commission_amount

FROM Orders o

JOIN Customer c ON o.customer_id = c.customer_id

JOIN Salesman s ON o.salesman_id = s.salesman_id

WHERE c.grade >= 200;

/* 8. Orders on a specific date */

SELECT *

FROM Customer c

JOIN Orders o

ON c.customer_id = o.customer_id

WHERE o.ord_date = '2012-10-05';