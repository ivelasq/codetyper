import pandas as pd
import numpy as np

data = {"name": ["Alice", "Bob", "Charlie"], "age": [25, 30, 35], "score": [85, 90, 95]}
df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)
print(f"\nMean age: {df['age'].mean()}")
