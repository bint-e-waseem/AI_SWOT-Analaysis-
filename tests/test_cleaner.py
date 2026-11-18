# Test 
if __name__ == "__main__":
    import pandas as pd
    
    print("Raw data load ho raha hai...")
    # Direct file read 
    df = pd.read_csv("data/raw/SuperMarket Analysis.csv")
    
    # Data clean karein
    cleaned_data = clean_data(df)
    
    # Cleaned data save
    cleaned_data.to_csv("data/processed/cleaned_supermarket_data.csv", index=False)
    print("💾 Cleaned data 'data/processed/' folder mein save ho gaya!")
    
    # 5 row
    print("\n--- Cleaned Data (Head) ---")
    print(cleaned_data.head())
