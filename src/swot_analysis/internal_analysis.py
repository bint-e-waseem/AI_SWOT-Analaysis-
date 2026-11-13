import pandas as pd

def analyze_internal_factors(df):
    """
    Analyzes internal data to identify Strengths and Weaknesses.
    """
    print("Analyzing internal business factors...")
    
    swot = {"Strengths": [], "Weaknesses": []}
    
    # Identify Top Performing Product Line (Strength)
    if 'Product line' in df.columns and 'Sales' in df.columns:
        top_product = df.groupby('Product line')['Sales'].sum().idxmax()
        top_sales = df.groupby('Product line')['Sales'].sum().max()
        swot["Strengths"].append(f"High revenue generation from '{top_product}' product line (Total Sales: {top_sales:.2f}).")
        
        # Identify Lowest Performing Product Line (Weakness)
        low_product = df.groupby('Product line')['Sales'].sum().idxmin()
        low_sales = df.groupby('Product line')['Sales'].sum().min()
        swot["Weaknesses"].append(f"Underperforming '{low_product}' product line (Total Sales: {low_sales:.2f}).")

    # Analyze Customer Ratings (Strength/Weakness)
    if 'Rating' in df.columns:
        avg_rating = df['Rating'].mean()
        if avg_rating >= 7.0:
            swot["Strengths"].append(f"High average customer satisfaction rating of {avg_rating:.2f}.")
        else:
            swot["Weaknesses"].append(f"Below average customer satisfaction rating of {avg_rating:.2f}.")

    # Analyze Gross Margin Percentage (Strength/Weakness)
    if 'gross margin percentage' in df.columns:
        avg_margin = df['gross margin percentage'].mean()
        # Assuming standard margin is around 4.7% based on the dataset
        if avg_margin > 4.5:
            swot["Strengths"].append(f"Healthy average gross margin percentage of {avg_margin:.2f}%.")
        else:
            swot["Weaknesses"].append(f"Low average gross margin percentage of {avg_margin:.2f}%.")

    return swot

if __name__ == "__main__":
    file_path = "data/processed/cleaned_supermarket_data.csv"
    try:
        df = pd.read_csv(file_path)
        internal_swot = analyze_internal_factors(df)
        
        print("\n--- Internal SWOT Analysis ---")
        print("\nStrengths:")
        for s in internal_swot["Strengths"]:
            print(f"- {s}")
            
        print("\nWeaknesses:")
        for w in internal_swot["Weaknesses"]:
            print(f"- {w}")
            
    except Exception as e:
        print(f"Error: {e}")