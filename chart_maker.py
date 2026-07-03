import matplotlib.pyplot as plt
import pandas as pd

def create_bar_chart(df, x_column, y_column, save_path="chart.png"):
    """
    Yeh function ek bar chart banata hai aur PNG file save karta hai.
    df: pandas DataFrame (data)
    x_column: x-axis pe kaunsa column dikhana hai (string)
    y_column: y-axis pe kaunsa column dikhana hai (string)
    save_path: chart kaha save karna hai (default = chart.png)
    """
    plt.figure(figsize=(8, 5))
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
    # Test data banate hain
    data = {
        "City": ["Delhi", "Mumbai", "Noida", "Pune"],
        "Sales": [200, 350, 150, 280]
    }
    df = pd.DataFrame(data)
    
    create_bar_chart(df, "City", "Sales", save_path="chart.png")