import pandas as pd

def clean_data(df):
    print("🧹 Data cleaning start...")
    
    # 1. Duplicate rows 
    initial_rows = df.shape[0]
    df = df.drop_duplicates()
    print(f"   - Duplicate rows : {initial_rows - df.shape[0]}")

    # 2. Missing values 
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)
    
    text_cols = df.select_dtypes(include=['object']).columns
    df[text_cols] = df[text_cols].fillna("Unknown")

    # 3.  format 
    for col in df.columns:
        if 'date' in col.lower():
            try:
                df[col] = pd.to_datetime(df[col])
                print(f"   - '{col}' column  Date format  convert.")
            except:
                print(f"   - '{col}' column  Date format donot convert")

    print("✅ Data cleaning compete!")
    return df

# Test 
if __name__ == "__main__":
    print("Raw data load ...")
    df = pd.read_csv("data/raw/SuperMarket Analysis.csv")
    
    # Data clean 
    cleaned_data = clean_data(df)
    
    # Cleaned data 
    cleaned_data.to_csv("data/processed/cleaned_supermarket_data.csv", index=False)
    print("💾 Cleaned data 'data/processed/' folder mein save ho gaya!")
    
    #5 rows
    print("\n--- Cleaned Data (Head) ---")
    print(cleaned_data.head())