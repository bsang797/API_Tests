import requests
import json

url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/stories/list"

querystring = {"template":"CURRENCY","id":"usdjpy"}

headers = {
    'x-rapidapi-host': "bloomberg-market-and-financial-news.p.rapidapi.com",
    'x-rapidapi-key': "c05dca0e2bmsh714d773e569e7b5p17b731jsnd45849212a46"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
news_json = json.dumps(response.json(), indent=4, separators=(". ", " = "))
print(news_json)