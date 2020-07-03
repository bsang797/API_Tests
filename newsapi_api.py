import requests
import json

#exchange = input("Enter the exchange of the company\n").upper()
#ticker = input("Enter the ticker of the company\n").upper()

exchange = "NASDAQ"
ticker = "AAPL"

response = requests.get(f"http://newsapi.org/v2/everything?q={exchange}:%20{ticker}&apiKey=29acf0f72d4c48a3a1ce38c0706980cc")
news_json = json.dumps(response.json(), indent=4, separators=(". ", " = "))
print(news_json)
