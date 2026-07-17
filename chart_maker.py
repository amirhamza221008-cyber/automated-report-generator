import matplotlib.pyplot as plt
import pandas as pd

def create_bar_chart(df, x_column, y_column, save_path="chart.png"):
    plt.figure(figsize=(10, 5))
    plt.bar(df[x_column], df[y_column], color="skyblue")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"{y_column} by {x_column}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"Chart saved as {save_path}")

if __name__ == "__main__":
    
    df = pd.read_csv("sample_data/household_power_consumption.csv", sep=",")

    
    df_small = df.head(10)

    # Real data se chart banana
    create_bar_chart(df_small, "Time", "Global_active_power", save_path="chart.png")