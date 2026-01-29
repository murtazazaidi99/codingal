Create Table  IMPLOY (
    product_name text
    supplies_ID text
    ph_no text
    Price text
);
Insert into IMPLOY(product_name,supplier_ID,ph_no,price)Values
('1','SYED','peshawer','*****',40),
('2','ALI','iran','***',90),
('3','MUHAMMAD','iraq','**',86);

select count(Product_address) as Product_count
from Product;

select avg(Price) as average_Price
from Product;

SELECT SUM(Price) as total_Price
from Product;