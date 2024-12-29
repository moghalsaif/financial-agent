from utils.data_fetcher import fetch_stock_data
from utils.data_processor import process_data
from utils.insights_generator import generate_insights

def main():
    # Fetch stock data (e.g., for NVIDIA)
    ticker = "NVDA"
    data = fetch_stock_data(ticker)
    if data is not None:
        # Process data
        processed_data = process_data(data)
        # Generate insights
        insights = generate_insights(processed_data)
        # Print insights
        print("Generated Insights:")
        print(insights)
    else:
        print("No data fetched. Check the ticker symbol or your internet connection.")

if __name__ == "__main__":
    main()
