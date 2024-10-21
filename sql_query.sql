SELECT name,
       price AS original_price,
       price + (price * 0.10) AS new_price
FROM products
ORDER BY name;
