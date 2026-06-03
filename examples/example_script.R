---
language: r
output_file: demo_from_script.R
typing_speed: 0.01
execute_blocks: true
---

## Load libraries
library(ggplot2)
library(dplyr)

## Create sample data | pause_after=1.5
data <- data.frame(
  x = 1:10,
  y = rnorm(10)
)

## Display and summarize | execute=true, pause_after=2.0
print(data)
cat("\nSummary statistics:\n")
summary(data)
