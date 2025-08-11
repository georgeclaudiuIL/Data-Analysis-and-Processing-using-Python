

import pandas as pd

file_path = "online_store_data.csv"
df = pd.read_csv(file_path)


numar_produse = df.shape[0]
print(f"Numarul total de produse din setul de date: {numar_produse}")


cel_mai_vandut = df.sort_values(by="quantity_sold", ascending=False).iloc[0]
print("\nCel mai bine vandut produs:")
print(cel_mai_vandut)


top_5_smartphones = (df[df["category"] == "Smartphones"].sort_values(by="quantity_sold", ascending=False).head(5))
print("\nTop 5 telefoane mobile vandute:")
print(top_5_smartphones[["product_name", "quantity_sold", "price"]])


laptops = df[(df["category"] == "Laptops") & (df["price"] > 0)]
pret_max = laptops["price"].max()
pret_min = laptops["price"].min()


print("\nPretul celui mai scump laptop:", pret_max)
print("Pretul celui mai ieftin laptop:", pret_min)
