Create Table Product (
    product_name text
    supplies_ID text
    ph_no text
    Price text
);
Insert into Product(product_name,supplier_address,ph_no,price)Values
('1','zaidi','peshawer','*****',20),
('2','abbas','iran','***',10),
('3','ali','iraq','**',56);

select count(Product_address) as Product_count
from Product;

select avg(Price) as average_Price
from Product;

SELECT SUM(Price) as total_Price
from Product;