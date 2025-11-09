# Legacy Data Migration 2021

This project demonstrates a real-world style data migration and transformation pipeline  
developed for a mid-size European food manufacturing client during 2021.

The goal was to consolidate historical CRM and transaction data from legacy systems  
(CSV exports, Access databases) into a unified PostgreSQL data warehouse.

All data in this repository is fully synthetic and for demonstration purposes only.

---

## Key Features
- Extracts legacy CSV data from local sources.  
- Cleans and normalizes customer emails, phones, and transaction amounts.  
- Loads validated records into staging tables in PostgreSQL.  
- Supports incremental updates for loyalty and sales dimensions.  
- Includes validation logic for data quality control.  

---

## Tech Stack
Python 3.8  
Pandas  
SQLAlchemy  
PostgreSQL  
dotenv  

---

## Usage
To run the pipeline locally:

python scripts/extract_legacy_data.py
python scripts/transform_clean.py
python scripts/validate_records.py
python scripts/load_to_postgres.py
All output logs and tables are written locally or to the configured PostgreSQL instance.

## Project Structure

scripts/  
extract_legacy_data.py — extract legacy CSV files  
transform_clean.py — normalize and clean datasets  
validate_records.py — check data quality and integrity  
load_to_postgres.py — load cleaned data into PostgreSQL  

sql/  
ddl_schema.sql — DDL for staging and core tables  
dim_loyalty.sql — loyalty dimension  
fact_sales.sql — sales fact aggregation  

data_sample/  
customers_legacy.csv — synthetic customers data  
transactions_legacy.csv — synthetic transactions data  
loyalty_cards.csv — synthetic loyalty program data  

---

## Disclaimer

This repository and its contents are for demonstration and educational purposes only.  
No proprietary or confidential company data, code, or structure is included.  
All dataset examples are artificially generated and do not correspond to real individuals or systems.
