### Part 2: SQL

1. Find all customers in Berlin
```SQL
SELECT * FROM Customers WHERE city = 'Berlin';
```

2. Find all customers in Mexico City
```SQL
SELECT * FROM Customers WHERE city LIKE 'México%';
```

3. Find avg price of all products
```SQL
SELECT AVG(price) AS "Average Price" FROM Products;
```

4. Find number of products that Have price = 18
```SQL
SELECT COUNT(*) AS "Number of products" FROM Products where price = 18;
```

5. Find orders between 1996-08-01 and 1996-09-06
```SQL
SELECT * FROM Orders WHERE OrderDate BETWEEN #08/01/1996# AND #09/06/1996#;
```

6. Find customers with more than 3 orders
```SQL
SELECT c.CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country FROM Orders o, Customers c WHERE c.CustomerId = o.CustomerId group by c.CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country having count(*) > 3;
```

7. Find all customers that are from the same city.
```SQL
SELECT * FROM Customers where City in (SELECT City from Customers group by City having count (*) >1) order by City;
```
