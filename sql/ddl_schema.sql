CREATE TABLE IF NOT EXISTS staging_customers (
    customer_id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    created_at DATE
);

CREATE TABLE IF NOT EXISTS staging_transactions (
    transaction_id SERIAL PRIMARY KEY,
    customer_id INT,
    amount NUMERIC(10,2),
    transaction_date DATE,
    loyalty_points INT
);

CREATE TABLE IF NOT EXISTS dim_loyalty (
    loyalty_id SERIAL PRIMARY KEY,
    customer_id INT,
    card_number TEXT UNIQUE,
    points_balance INT
);

CREATE TABLE IF NOT EXISTS fact_sales (
    sale_id SERIAL PRIMARY KEY,
    customer_id INT,
    transaction_id INT,
    total NUMERIC(10,2),
    date_id DATE
);
