This repository contains three data processing scripts:

1. Weather Data Aggregator
2. Prime Factorization Calculator
3. SQL Query for Product Price Increase

## 1. Weather Data Aggregator

### Setup

1. Ensure you have Python 3.x installed on your system.
2. Save the script as `weather_aggregator.py`.

### Running the Application

1. Open a terminal or command prompt.
2. Navigate to the directory containing `weather_aggregator.py`.
3. Run the script:

   ```bash
   python weather_aggregator.py
   ```

4. Follow the prompts to enter weather data for various cities.
5. Press Enter without entering a city name to finish input and see the results.

## 2. Prime Factorization Calculator

### Setup

1. Ensure you have Python 3.x installed on your system.
2. Save the script as `prime_factorization.py`.

### Running the Application

1. Open a terminal or command prompt.
2. Navigate to the directory containing `prime_factorization.py`.
3. Run the script:

   ```bash
   python prime_factorization.py
   ```

4. Enter positive integers when prompted to see their prime factorization.
5. Enter 0 to exit the program.

## 3. SQL Query for Product Price Increase

### Setup

1. Ensure you have access to a SQL database with a table named `products` containing `columns id`, `name`, and `price`.
2. Connect to your database using your preferred SQL client.

### Running the Query

1. Copy the following SQL query:

   ```sql
   SELECT name,
          price AS original_price,
          price + (price * 0.10) AS new_price
   FROM products
   ORDER BY name;
   ```

2. Paste the query into your SQL client.
3. Execute the query to see the results.

> **Note:** This query only displays the results and does not update the actual prices in the database.
