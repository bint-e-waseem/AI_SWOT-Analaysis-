import pandas as pd

def clean_data(df):
    
    print("🧹 Data cleaning shuru ho rahi hai...")
    
    # 1. Duplicate rows remove
    initial_rows = df.shape[0]
    df = df.drop_duplicates()
    print(f"   - Duplicate rows hataye gaye: {initial_rows - df.shape[0]}")

    # 2. Missing values ko handle karo
    
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)
    
    # Text columns mein missing values ko "Unknown" se replace karo
    text_cols = df.select_dtypes(include=['object']).columns
    df[text_cols] = df[text_cols].fillna("Unknown")


    for col in df.columns:
        if 'date' in col.lower():
            try:
                df[col] = pd.to_datetime(df[col])
                print(f"   - '{col}' column ko Date format mein convert kar diya gaya.")
            except:
                print(f"   - '{col}' column ko Date format mein convert nahi kiya ja saka.")

    print("✅ Data cleaning mukammal ho gayi!")
    return df

# Test 
if __name__ == "__main__":
    from src.data_processing.loader import load_data
    
    file_path = "data/raw/SuperMarket Analysis.csv"
    raw_data = load_data(file_path)
    
    if raw_data is not None:
        cleaned_data = clean_data(raw_data)
        
        
        cleaned_data.to_csv("data/processed/cleaned_supermarket_data.csv", index=False)
        print("💾 Cleaned data 'data/processed/' folder mein save ho gaya!")
        
        #  5 rows 
        print("\n--- Cleaned Data (Head) ---")
        print(cleaned_data.head())