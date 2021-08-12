import pandas as pd

def validate_data(customers, transactions):
    missing_emails = customers[customers["email"].isnull()]
    invalid_amounts = transactions[transactions["amount"] <= 0]

    print(f"⚠️ Missing emails: {len(missing_emails)} | Invalid transactions: {len(invalid_amounts)}")

if __name__ == "__main__":
    c = pd.read_csv("data_sample/customers_legacy.csv")
    t = pd.read_csv("data_sample/transactions_legacy.csv")
    validate_data(c, t)
