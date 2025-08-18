import pandas as pd


df = pd.read_csv("online_store_data.csv")

# conversii de tip
df["quantity_sold"] = pd.to_numeric(df["quantity_sold"], errors="coerce").fillna(0).astype(int)
df["num_of_ratings"] = pd.to_numeric(df["num_of_ratings"], errors="coerce").fillna(0).astype(int)

# quantity_in_stock în int
df["quantity_in_stock"] = pd.to_numeric(df["quantity_in_stock"], errors="coerce").fillna(0).astype(int)

# date_added în datetime
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# extragem doar numarul (8.5 out of 10 => 8.5)
df["rating"] = df["rating"].str.extract(r'(\d+\.?\d*)').astype(float)


# eliminam randurile fara product_name
df = df.dropna(subset=["product_name"])

# eliminam randurile cu mai multe de 4 valori lipsa
df = df.dropna(thresh=len(df.columns) - 4)

# eliminam duplicatele
df = df.drop_duplicates()

df["revenue"] = df["price"] * df["quantity_sold"]


# top 10 keyboards dupa venit
top_keyboards = df[df["category"] == "Keyboards"].sort_values("revenue", ascending=False).head(10)

# top 10 TVs cu venit minim
low_tvs = df[df["category"] == "TVs"].sort_values("revenue", ascending=True).head(10)

# 6. afisam rezultatele
print("Top 10 Keyboards dupa venit:")
print(top_keyboards[["product_name", "revenue"]])

print("\nTop 10 TVs cu cel mai mic venit:")
print(low_tvs[["product_name", "revenue"]])
