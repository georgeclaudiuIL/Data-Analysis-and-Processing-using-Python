

import pandas as pd
import numpy as np

# Incarcare date
df = pd.read_csv("online_store_data.csv")

# Convertim coloana rating (ex: "8.5 out of 10") in float
if "rating" in df.columns:
    df["rating_num"] = df["rating"].str.extract(r"(\d+\.?\d*)").astype(float)
else:
    df["rating_num"] = np.nan

# 1 Diferenta dintre cel mai bine si cel mai slab evaluat televizor
tvs = df[df["category"].str.contains("TV", case=False, na=False)]
if not tvs.empty:
    min_rating = tvs["rating_num"].min()
    max_rating = tvs["rating_num"].max()
    print("1 Range rating TV =", round(max_rating - min_rating, 2), "(min =", min_rating, ", max =", max_rating, ")")
else:
    print("1 Nu exista produse in categoria TV")

# 2 Intervalul intercuartil pentru preturile telefoanelor mobile
phones = df[df["category"].str.contains("smartphone|phone|mobile", case=False, na=False)]
if not phones.empty:
    q1 = phones["price"].quantile(0.25)
    q3 = phones["price"].quantile(0.75)
    print("2 Interval intercuartil pret Smartphones: [", q1, ",", q3, "]  IQR =", q3 - q1)
else:
    print("2 Nu exista produse in categoria Smartphones")

# 3 Cele 5 branduri cu cele mai uniforme evaluari (abatere standard minima)
if "brand" in df.columns and "rating_num" in df.columns:
    brand_std = df.groupby("brand")["rating_num"].std().dropna().sort_values()
    top5 = brand_std.head(5)
    print("3 Top 5 branduri cu cele mai uniforme evaluari (std rating):")
    print(top5)
else:
    print("3 Lipsesc coloanele brand sau rating pentru calcul")

# 4 Relatia intre numarul de evaluari si numarul de unitati vandute
if "num_of_ratings" in df.columns and "quantity_sold" in df.columns:
    df["quartile"] = pd.qcut(df["num_of_ratings"].rank(method="first"), 4, labels=["1st quartile","2nd quartile","3rd quartile","4th quartile"])
    grouped = df.groupby("quartile")["quantity_sold"].sum()
    print("4) Totalul unitatilor vandute pe cvartile de numar de evaluari:")
    print(grouped)
else:
    print("4 Lipsesc coloanele necesare pentru analiza (num_of_ratings sau quantity_sold)")
