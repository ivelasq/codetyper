"""Template scripts for initialization."""

PYTHON_TEMPLATE = '''---
language: python
output_file: demo.py
typing_speed: 0.05
execute_blocks: true
---

## Import libraries
import pandas as pd
import numpy as np

## Load data | pause_after=1.5
# Add your data loading code here
data = {
    'x': range(1, 11),
    'y': np.random.randn(10)
}
df = pd.DataFrame(data)

## Process and display | execute=true, pause_after=2.0
# Add your analysis code here
print(df)
print(df.describe())
'''

R_TEMPLATE = '''---
language: r
output_file: demo.R
typing_speed: 0.05
execute_blocks: true
---

## Setup
library(ggplot2)
library(dplyr)

## Load data | pause_after=1.5
# Add your data loading code here
data <- data.frame(
  x = 1:10,
  y = rnorm(10)
)

## Process and visualize | execute=true, pause_after=2.0
# Add your analysis code here
print(data)
summary(data)
'''

TEMPLATES = {
    'python': PYTHON_TEMPLATE,
    'r': R_TEMPLATE,
}
