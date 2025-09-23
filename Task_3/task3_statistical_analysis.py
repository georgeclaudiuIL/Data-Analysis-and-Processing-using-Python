

import pandas as pd

# incarcare CSV
df = pd.read_csv("online_store_data.csv")

# conversii de coloane
df["rating"] = df["rating"].str.extract(r"([0-9.]+)").astype(float)   # extrage numarul din text
df["quantity_in_stock"] = pd.to_numeric(df["quantity_in_stock"], errors="coerce").fillna(0).astype(int)
df["quantity_sold"] = pd.to_numeric(df["quantity_sold"], errors="coerce").fillna(0).astype(int)

# 1. Media ratingurilor
print("Media ratingurilor:", round(df["rating"].mean(), 2))

# 2. Cel mai frecvent brand
print("Cel mai frecvent brand:", df["brand"].mode()[0])

# 3. Cel mai vandut brand
best_selling = df.groupby("brand")["quantity_sold"].sum().idxmax()
print("Cel mai vandut brand:", best_selling)

# 4. Media ratingurilor pe categorii
print("\nMedia ratingurilor pe categorii:")
print(round(df.groupby("category")["rating"].mean(), 2))

# 5. Popularitatea pe culori
print("\nPopularitatea pe culori (unitati vandute):")
print(df.groupby("color")["quantity_sold"].sum().sort_values(ascending=False))

# 6. Top 5 branduri eficiente
brands = df.groupby("brand").agg({"quantity_sold": "sum", "quantity_in_stock": "sum"})
brands["efficiency"] = brands["quantity_sold"] / (brands["quantity_sold"] + brands["quantity_in_stock"])
print("\nTop 5 branduri eficiente:")
print(brands.sort_values("efficiency", ascending=False).head(5))

