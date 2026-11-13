def analyze_external_factors():
    """
    Defines external market factors (Opportunities and Threats).
    In a real-world scenario, these would be derived from market research or news APIs.
    """
    print("Analyzing external market factors...")
    
    swot = {
        "Opportunities": [
            "Expansion into new geographic markets or cities.",
            "Introduction of loyalty programs to retain high-value customers.",
            "Partnerships with local businesses for cross-promotion."
        ],
        "Threats": [
            "Increasing competition from online retailers.",
            "Rising operational costs and inflation.",
            "Changes in consumer spending behavior due to economic conditions."
        ]
    }
    
    return swot

if __name__ == "__main__":
    external_swot = analyze_external_factors()
    
    print("\n--- External SWOT Analysis ---")
    print("\nOpportunities:")
    for o in external_swot["Opportunities"]:
        print(f"- {o}")
        
    print("\nThreats:")
    for t in external_swot["Threats"]:
        print(f"- {t}")