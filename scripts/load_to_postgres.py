import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL", "postgresql://user:password@localhost:5432/mlinotest")

def load_data():
    engine = create_engine(DB_URL)
    customers = pd.read_csv("data_sample/customers_legacy.csv")
    transactions = pd.read_csv("data_sample/transactions_legacy.csv")

    customers.to_sql("staging_customers", engine, if_exists="append", index=False)
    transactions.to_sql("staging_transactions", engine, if_exists="append", index=False)
    print("Data successfully loaded to PostgreSQL")

if __name__ == "__main__":
    load_data()
