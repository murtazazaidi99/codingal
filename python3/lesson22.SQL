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

SELECT customer.cust_name,salesman.name,salesman.city
FROM Customer
JOIN Salesman ON Customer.city=Salesman.city;

SELECT Customer.cust_name,Salesman.name
FROM Customer
JOIN Salesman ON Customer.Salesman_id=Salesman.Salesman_id;

SELECT Order.ord_no,Customer.cust_name,Order.customer_id,Order.Salesman_id
FROM Orders
JOIN customer ON Order.customer_ig=Customer.customer_id
JOIN Salesman ON Order.Salesman_id=Salesman.Salesman_id
WHERE Customer.city <> Salesman.city;


SELECT *
FROM Customer \
JOIN Orders ON Customer_id=Order.customer_id
WHERE Orders.ord_date='2001-12-30';