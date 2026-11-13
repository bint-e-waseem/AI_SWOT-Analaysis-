import pandas as pd

def calculate_kpis(df):
    """
    Yeh function business ke important KPIs (Key Performance Indicators) calculate karta hai.
    """
    print("📊 Business KPIs calculate kiye ja rahe hain...")
    
    kpis = {}
    
    
    if 'Total' in df.columns:
        kpis['Total Sales'] = df['Total'].sum()
    elif 'gross income' in df.columns:
        kpis['Total Sales'] = df['gross income'].sum()
    else:
        kpis['Total Sales'] = "Column not found"

    
    if 'Rating' in df.columns:
        kpis['Average Rating'] = round(df['Rating'].mean(), 2)
    else:
        kpis['Average Rating'] = "N/A"

    
    kpis['Total Transactions'] = len(df)

    
    if 'Product line' in df.columns and 'Total' in df.columns:
        kpis['Top Product Line'] = df.groupby('Product line')['Total'].sum().idxmax()
    
    
    if 'Gender' in df.columns and 'Total' in df.columns:
        gender_sales = df.groupby('Gender')['Total'].sum()
        kpis['Sales by Gender'] = gender_sales.to_dict()

    print("✅ KPIs successfully calculate ho gaye!")
    return kpis


if __name__ == "__main__":
    
    file_path = "data/processed/cleaned_supermarket_data.csv"
    
    try:
        df = pd.read_csv(file_path)
        results = calculate_kpis(df)
        
        # Print the results
        print("\n--- Business KPIs ---")
        for key, value in results.items():
            print(f"🔹 {key}: {value}")
            
    except FileNotFoundError:
        print(f" Error: '{file_path}' nahi mili. Pehle cleaner.py run karein.")