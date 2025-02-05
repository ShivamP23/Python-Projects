import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# STOCK_APT_KEY = use your own key visiting the website
# NEWS_API_KEY = use your own key by visting the website 

stock_params = {
   "function": "TIME_SERIES_DAILY",
   "symbol": STOCK_NAME,
   "apikey": STOCK_APT_KEY
}

response = requests.get(STOCK_ENDPOINT, stock_params)
#print(weather_data["list"][0]["weather"][0]["id"])
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday = data_list[1]
day_before_closing = day_before_yesterday["4. close"]
print(day_before_closing)


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) - float(day_before_closing)) 
print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 2:
    news_params = {
        "apiKey" : NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params= news_params) 
    articles = news_response.json()["articles"]
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
three_articles = articles[:3]
print(three_articles)

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"Headline: {articles['title']}. \nBrief: {articles['description']}" for articles in three_articles]

#TODO 9. - Send each article as a separate message via Twilio. 
#use your own twilio account to do this part.



# "TRHH5NZ9LYZY6K57"
# "eba2e196d1d9492aae2fe0fa76d1de86"