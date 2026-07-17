import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def generate_summary(df):
    """
    Yeh function CSV data ka automatic summary banata hai
    """
    stats = df.describe()
    
    avg_power = round(df['Global_active_power'].mean(), 2)
    max_power = round(df['Global_active_power'].max(), 2)
    min_power = round(df['Global_active_power'].min(), 2)
    avg_voltage = round(df['Voltage'].mean(), 2)
    total_records = len(df)

    summary = f"""Executive Summary - Household Power Consumption Analysis

This report analyzes {total_records} records of household power consumption data.

Key Findings:
- Average Global Active Power: {avg_power} kilowatts
- Peak Power Consumption: {max_power} kilowatts  
- Minimum Power Consumption: {min_power} kilowatts
- Average Voltage: {avg_voltage} volts

The data indicates typical household energy usage patterns with power consumption 
ranging from {min_power} kW to {max_power} kW. Average consumption of {avg_power} kW 
suggests moderate energy usage throughout the recorded period.

Recommendation: Monitor peak usage hours to optimize energy consumption and reduce costs.
"""
    
    print("Summary Generated!")
    print(summary)
    return summary


if __name__ == "__main__":
    df = pd.read_csv("sample_data/household_power_consumption.csv")
    generate_summary(df)