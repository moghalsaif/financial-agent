import pandas as pd

def process_data(data):
    """
    Process the fetched stock data.

    Parameters:
        data (dict): A dictionary containing recommendations and news.

    Returns:
        dict: Processed data.
    """
    processed_data = {}
    
    # Process recommendations
    if data["recommendations"] is not None:
        recommendations = data["recommendations"]
        # Summarize the recommendations
        processed_data["recommendations"] = {
            "strongBuy": recommendations["strongBuy"].mean(),
            "buy": recommendations["buy"].mean(),
            "hold": recommendations["hold"].mean(),
            "sell": recommendations["sell"].mean(),
            "strongSell": recommendations["strongSell"].mean(),
        }
    
    # Process news
    if data["news"]:
        news = data["news"]
        # Extract relevant fields dynamically (without links)
        processed_data["news"] = [
            {
                "title": item.get("title", "No title"),
                "publisher": item.get("publisher", "Unknown publisher"),
            }
            for item in news[:5]  # Get the latest 5 news items
        ]
    
    return processed_data
