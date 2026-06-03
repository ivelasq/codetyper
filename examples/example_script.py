---
language: python
output_file: /Users/isabella.velasquez/typr-test/demo_from_script.py
typing_speed: 0.01
execute_blocks: true
format_output: true
---

## Setup libraries
import pandas as pd
import numpy as np

## Create sample data | pause_after=1.5
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'score': [85, 90, 95]
}
df = pd.DataFrame(data)

## Display results | execute=true, pause_after=2.0
print("Sample DataFrame:")
print(df)
print(f"\nMean age: {df['age'].mean()}")
