import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import pytest
from datetime import datetime
import random
import csv

# calling / reading the data
df = pd.read_csv(r'C:\Users\user\OneDrive\Desktop\CSE111\Sample\logged_time.csv')
print(df)
# Ensure the file exists and is loaded correctly
if df.empty:
    print("The DataFrame is empty. Please check the file path or content.")
else:
    print("DataFrame loaded successfully.")
df



# Define temperature and humidity for demonstration purposes
temperature = 25  # Example temperature value
humidity = 60     # Example humidity value

# Write the DataFrame and additional data to a file
with open("output.txt", "at") as output_file:
    print(df, file=output_file)
    print(f"{temperature}, {humidity}", file=output_file)
    # Example: Uncomment and define variables if needed
    # file.write(f"{city_name}, {elevation},{population},{cities_file}")
