import pandas as pd

def load_data(file_path):

    df = pd.read_csv(file_path)
    return df

def analyze(df):
    # Basic stats nikalo
    stats = {
        "total_rows": len(df),
        "columns": list(df.columns),
        "summary": df.describe().to_dict()
    }
    return stats


if __name__ == "__main__":
    file_path = "sample_data/household_power_consumption.csv"
    
    df = load_data(file_path)
    
    print("Total rows:", len(df))
    print("\nColumns hain:")
    print(df.columns.tolist())
    
    print("\nPehle 5 rows:")
    print(df.head())
    
    print("\nBasic statistics:")
    print(df.describe())