import pandas as pd

def clean_customers(df):
    df["email"] = df["email"].str.lower().str.strip()
    df["phone"] = df["phone"].str.replace(r"\D+", "", regex=True)
    df = df.drop_duplicates(subset=["email"])
    return df

def clean_transactions(df):
    df = df[df["amount"] > 0]
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])
    return df

if __name__ == "__main__":
    c = pd.read_csv("data_sample/customers_legacy.csv")
    t = pd.read_csv("data_sample/transactions_legacy.csv")
    c = clean_customers(c)
    t = clean_transactions(t)
    print("Cleaned customers:", c.shape[0], "| transactions:", t.shape[0])
