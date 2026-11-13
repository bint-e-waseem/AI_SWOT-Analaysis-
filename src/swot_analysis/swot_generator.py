import pandas as pd
import sys
import os

# Get the absolute path of the current directory (src/swot_analysis)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the current directory and the project root to sys.path
sys.path.append(current_dir)
sys.path.append(os.path.abspath(os.path.join(current_dir, '..', '..')))

# Now import directly from the same folder
from internal_analysis import analyze_internal_factors
from external_analysis import analyze_external_factors


def generate_full_swot(df):
    """
    Combines internal and external analysis to generate a complete SWOT report.
    """
    print("Generating comprehensive SWOT analysis...")
    
    # Get internal and external factors
    internal_swot = analyze_internal_factors(df)
    external_swot = analyze_external_factors()
    
    # Combine into a single dictionary
    full_swot = {
        "Strengths": internal_swot.get("Strengths", []),
        "Weaknesses": internal_swot.get("Weaknesses", []),
        "Opportunities": external_swot.get("Opportunities", []),
        "Threats": external_swot.get("Threats", [])
    }
    
    return full_swot

def print_swot_report(swot):
    """
    Prints the SWOT analysis in a structured format.
    """
    print("\n" + "="*40)
    print("COMPLETE SWOT ANALYSIS REPORT")
    print("="*40)
    
    for category, items in swot.items():
        print(f"\n[{category.upper()}]")
        if not items:
            print("- No significant factors identified.")
        for item in items:
            print(f"  * {item}")

if __name__ == "__main__":
    file_path = "data/processed/cleaned_supermarket_data.csv"
    
    try:
        print("Loading data for SWOT analysis...")
        df = pd.read_csv(file_path)
        
        # Generate SWOT
        final_swot = generate_full_swot(df)
        
        # Print the report
        print_swot_report(final_swot)
        
        # Save the SWOT to a text file in the reports folder
        with open('reports/swot_report.txt', 'w') as f:
            f.write("COMPLETE SWOT ANALYSIS REPORT\n")
            f.write("="*40 + "\n")
            for category, items in final_swot.items():
                f.write(f"\n[{category.upper()}]\n")
                for item in items:
                    f.write(f"  * {item}\n")
        print("\nSWOT Report saved to 'reports/swot_report.txt'.")
        
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please run cleaner.py first.")
    except ImportError as e:
        print(f"Import Error: {e}. Make sure all files are in the correct folders.")