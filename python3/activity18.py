
# Create two tables "Salesman" & "Orders" and then write a query to display all the orders for the salesman who belongs to the city London.
CREATE table Salesman(
    Salesman_id INT PRIMARY KEY,
    NAME VARCHAR(30),
    CITY VARCHAR(30),
    COMMISSION DECIMAL(20,2)
);
INSERT INFO Salesman VALUES(5001, 'JAMES HOOG', 'NEW YORK', 0.15);
,(5002, 'NATHAN BELL', 'LANDON',0.13);
CREATE TABLE IF NOT EXISTS Salesman(
Salesman_id INT PRIMARY KEY,
Name VARCHAR(20),
City VARCHAR(20),
# Commission DECIMAL(10,2) REAL
);
INSERT INTO Salesman VALUES (1001, 'James Hoog', 'New York', 0.15), (1002, 'Nail Knite', 'Paris', 0.13), (1005, 'Pit Alex', 'London', 0.11), (1006, 'Mc Lyon', 'Paris', 0.14), (1007, 'Paul Adam', 'Rome', 0.13);
SELECT * FROM Salesman;
CREATE TABLE IF NOT EXISTS Orders(
Ord_no INT PRIMARY KEY,
Purch_amt DECIMAL(10,2),
Ord_date DATE,
Customer_id INT,
Salesman_id INT,
)
INSERT INTO Orders VALUES (70001, 150.5, '2012-10-05', 3005, 5002), (70009, 270.65, '2012-09-10', 3001, 5005), (70002, 65.26, '2012-10-05', 3002, 5001),(70004, 110.5, '2012-08-17', 3009, 5003);
SELECT * FROM Orders;