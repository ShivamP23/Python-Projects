# Stock Price & News Alert Script

This is a Python script that checks Tesla's stock price changes and fetches relevant news articles if there's a significant price movement.

## Requirements
- Python 3.x
- `requests` library (install with `pip install requests`)

## Setup
1. Get an API key from [Alpha Vantage](https://www.alphavantage.co/) for stock data.
2. Get an API key from [NewsAPI](https://newsapi.org/) for news articles.
3. Replace `STOCK_APT_KEY` and `NEWS_API_KEY` in the script with your actual API keys.

## How It Works
- **Fetches Tesla's Stock Data** from Alpha Vantage
- **Calculates Price Change** between yesterday and the day before
- **Checks for Significant Movement** (greater than 2%)
- **Fetches News Articles** if the stock movement threshold is met
- **Sends News Updates via Text Message** (requires Twilio integration)

## Usage
1. Make sure you have set up your API keys correctly.
2. Run the script:
   ```bash
   python script.py
   ```
3. If the stock price changes by more than 2%, you'll receive news updates via text message.

## Notes
- You can adjust the stock movement threshold by modifying the percentage in the script.
- The script fetches the top 3 news articles related to Tesla Inc.
- Make sure to integrate a messaging service like Twilio to receive news alerts.

## Example Response
If Tesla's stock price changes significantly, you will receive a text message like this:
```
Headline: Tesla Stock Soars Amid Market Optimism.
Brief: Tesla's stock jumped 5% following strong earnings results...
```


