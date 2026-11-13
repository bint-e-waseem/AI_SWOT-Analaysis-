import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charts 
sns.set_theme(style="darkgrid")

def generate_eda_charts(df):
    """
    Yeh function data se mukhtalif charts banata hai aur unko 'reports/' folder mein save karta hai.
    """
    print("📈 EDA Charts banaye ja rahe hain...")
    
    # 1. Sales by Product Line (Bar Chart)
    if 'Product line' in df.columns and 'Total' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.barplot(data=df, x='Product line', y='Total', estimator=sum, errorbar=None, palette='viridis')
        plt.title('Total Sales by Product Line')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('reports/sales_by_product_line.png')
        plt.close()
        print("   ✅ 'sales_by_product_line.png' save ho gaya.")

    # 2. Sales by Gender (Pie Chart)
    if 'Gender' in df.columns and 'Total' in df.columns:
        plt.figure(figsize=(8, 8))
        gender_sales = df.groupby('Gender')['Total'].sum()
        plt.pie(gender_sales, labels=gender_sales.index, autopct='%1.1f%%', colors=['#66b3ff','#ff9999'])
        plt.title('Sales Distribution by Gender')
        plt.savefig('reports/sales_by_gender.png')
        plt.close()
        print("   ✅ 'sales_by_gender.png' save ho gaya.")

    
    if 'Payment' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df, x='Payment', palette='pastel')
        plt.title('Payment Method Distribution')
        plt.tight_layout()
        plt.savefig('reports/payment_method_distribution.png')
        plt.close()
        print("    'payment_method_distribution.png' save ho gaya.")

    print(" Tamam charts 'reports/' folder mein save ho gaye hain!")

# Test 
if __name__ == "__main__":
    file_path = "data/processed/cleaned_supermarket_data.csv"
    
    try:
        print("Cleaned data load ho raha hai...")
        df = pd.read_csv(file_path)
        generate_eda_charts(df)
    except FileNotFoundError:
        print(f" Error: '{file_path}' nahi mili. Pehle cleaner.py run karein.")