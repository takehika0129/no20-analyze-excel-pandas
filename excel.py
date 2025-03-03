import pandas as pd
import numpy as np

np.random.seed(42)
num_rows = 100


data = {
    "ID": range(1, num_rows + 1),
    "Date": pd.date_range(start="2021-01-01", periods=num_rows, freq="D"),
    "Region": np.random.choice(["North", "South", "East", "West"], size=num_rows),
    "Product": np.random.choice(["Product A", "Product B", "Product C", "Product D"], size=num_rows),
    "Category": np.random.choice(["Category 1", "Category 2", "Category 3"], size=num_rows),
    "Sales": np.random.randint(100, 2000, size=num_rows),
    "Quantity": np.random.randint(1, 25, size=num_rows),
    "Payment Method": np.random.choice(["Cash", "Credit", "Online"], size=num_rows)
}

df = pd.DataFrame(data)
df['Price_per_Unit'] = df['Sales'] / df['Quantity']

df.to_excel("sample_data.xlsx", index=False)

print("Excel file 'sample_data.xlsx' has been created with 100 rows and 9 columns.")
