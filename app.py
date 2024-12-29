import streamlit as st
from utils.data_fetcher import fetch_stock_data
from utils.data_processor import process_data
from utils.insights_generator import generate_insights

# Streamlit app title
st.title("Financial Agent: Stock Insights")

# Input for the stock ticker
ticker = st.text_input("Click the button to get insights on NVDA Stock (e.g., NVDA):", "NVDA")

# Button to fetch and analyze data
if st.button("Get Insights"):
    if ticker:
        with st.spinner("Fetching data and generating insights..."):
            # Fetch stock data
            data = fetch_stock_data(ticker)
            if data is not None:
                # Process data
                processed_data = process_data(data)
                # Generate insights
                insights = generate_insights(processed_data)
                if insights:
                    # Display insights
                    st.success("Insights generated successfully!")
                    st.markdown("### Analyst Recommendations")
                    st.write(processed_data["recommendations"])
                    st.markdown("### Latest News")
                    for news_item in processed_data["news"]:
                        st.write(f"**{news_item['title']}**")
                        st.write(f"Publisher: {news_item['publisher']}")
                    st.markdown("### Generated Insights")
                    st.write(insights)
                else:
                    st.error("Failed to generate insights. Please try again.")
            else:
                st.error("Failed to fetch data. Please check the ticker symbol or your internet connection.")
    else:
        st.warning("Please enter a valid stock ticker.")
