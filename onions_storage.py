# Importing Statements
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
df

# load_optimal_ranges() Function
def load_optimal_ranges():
    """Returns a dictionary containing the optimal temperature and humidity ranges for onions."""
    return {
        "temperature": (0, 4),  # Optimal temperature in Celsius (example range)
        "humidity": (65, 70)      # Optimal relative humidity in percentage (example range)
    }

def simulate_current_conditions():
    """Generates and returns simulated current temperature and humidity readings."""
    temperature = random.uniform(-5, 10)
    humidity = random.uniform(50, 80)
    return temperature, humidity

# Calling Test fuctions for temperature: test_check_temperature_status
def check_temperature_status(current_temp, optimal_temp_range):
    """Checks the current temperature against the optimal range and returns a status."""
    min_temp, max_temp = optimal_temp_range
    if current_temp < min_temp:
        return "Too Low"
    elif current_temp > max_temp:
        return "Too High"
    else:
        return "Optimal"

# Calling test fuctions for relative humidity: test_check_humidity_status
def check_humidity_status(current_humidity, optimal_humidity_range):
    """Checks the current humidity against the optimal range and returns a status."""
    min_humidity, max_humidity = optimal_humidity_range
    if current_humidity < min_humidity:
        return "Too Low"
    elif current_humidity > max_humidity:
        return "Too High"
    else:
        return "Optimal"

# determine_action() Function
def determine_action(status_indicator):
    """Suggests a corrective action based on the status indicator."""
    if status_indicator == "Too High":
        return "Increase ventilation or activate cooling."
    elif status_indicator == "Too Low":
        return "Decrease ventilation or activate heating/humidification."
    else:
        return "No action needed."

# display_status() Function
def display_status(current_temp, current_humidity, temp_status, humidity_status, temp_action, humidity_action):
    """Prints a formatted status report to the user."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n--- Onion Storage Environment Status ---")
    print(f"Timestamp: {timestamp}")
    print(f"Current Temperature: {current_temp:.2f}°C")
    print(f"Temperature Status: {temp_status}")
    if temp_action:
        print(f"Suggested Action (Temperature): {temp_action}")
    print(f"\nCurrent Humidity: {current_humidity:.2f}% RH")
    print(f"Humidity Status: {humidity_status}")
    if humidity_action:
        print(f"Suggested Action (Humidity): {humidity_action}")
    print("----------------------------------------")

def main():
    """Orchestrates the onion storage environment monitoring program using data from the DataFrame."""
    optimal_ranges = load_optimal_ranges()

    print(f"Processing data from DataFrame:")
    for index, row in df.iterrows():
        try:
            current_temperature = float(row['Temperature'])
            current_humidity = float(row['Humidity'])

            temp_status = check_temperature_status(current_temperature, optimal_ranges["temperature"])
            humidity_status = check_humidity_status(current_humidity, optimal_ranges["humidity"])

            temp_action = determine_action(temp_status)
            humidity_action = determine_action(humidity_status)

            display_status(current_temperature, current_humidity, temp_status, humidity_status, temp_action, humidity_action)

        except ValueError:
            print(f"Skipping row at index {index} due to invalid temperature or humidity data.")
        except KeyError as e:
            print(f"Error: Column '{e}' not found in the DataFrame.")
            return

# --- Test Functions using pytest ---
def test_check_temperature_status():
    optimal_range = (0, 4)
    assert check_temperature_status(-1, optimal_range) == "Too Low"
    assert check_temperature_status(2, optimal_range) == "Optimal"
    assert check_temperature_status(5, optimal_range) == "Too High"
    assert check_temperature_status(0, optimal_range) == "Optimal"
    assert check_temperature_status(4, optimal_range) == "Optimal"

def test_check_humidity_status():
    optimal_range = (65, 70)
    assert check_humidity_status(60, optimal_range) == "Too Low"
    assert check_humidity_status(68, optimal_range) == "Optimal"
    assert check_humidity_status(75, optimal_range) == "Too High"
    assert check_humidity_status(65, optimal_range) == "Optimal"
    assert check_humidity_status(70, optimal_range) == "Optimal"

if __name__ == "__main__":
    main()
