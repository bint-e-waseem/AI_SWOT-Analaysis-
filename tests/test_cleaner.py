# Test karne ke liye
if __name__ == "__main__":
    import pandas as pd
    
    print("Raw data load ho raha hai...")
    # Direct file read kar rahe hain taake import ka masla na aaye
    df = pd.read_csv("data/raw/SuperMarket Analysis.csv")
    
    # Data clean karein
    cleaned_data = clean_data(df)
    
    # Cleaned data ko data/processed folder mein save karein
    cleaned_data.to_csv("data/processed/cleaned_supermarket_data.csv", index=False)
    print("💾 Cleaned data 'data/processed/' folder mein save ho gaya!")
    
    # Pehli 5 rows dikhayein
    print("\n--- Cleaned Data (Head) ---")
    print(cleaned_data.head())