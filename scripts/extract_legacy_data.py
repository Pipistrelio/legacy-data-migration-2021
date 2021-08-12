import pandas as pd
from pathlib import Path

def extract_legacy_data():
    base_path = Path(__file__).resolve().parents[1] / "data_sample"

    customers = pd.read_csv(base_path / "customers_legacy.csv")
    transactions = pd.read_csv(base_path / "transactions_legacy.csv")
    loyalty = pd.read_csv(base_path / "loyalty_cards.csv")

    print(f"Extracted: {len(customers)} customers, {len(transactions)} transactions, {len(loyalty)} loyalty records.")
    return customers, transactions, loyalty

if __name__ == "__main__":
    extract_legacy_data()
