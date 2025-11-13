import pandas as pd
import matplotlib.pyplot as plt

data = {
    "category": ["Electronics", "Clothing", "Groceries", "Electronics", "Clothing"],
    "sales": [15000, 8000, 12000, 20000, 9000]
}

df = pd.DataFrame(data)

category_sales = df.groupby("category")["sales"].sum()

category_sales.plot(kind="bar")

plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.title("Total Sales Per Category")
plt.show()
