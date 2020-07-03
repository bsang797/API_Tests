import json
import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-news"

querystring = {"region":"US","category":"MSFT"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "c05dca0e2bmsh714d773e569e7b5p17b731jsnd45849212a46"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
news_json = json.dumps(response.json(), indent=4, separators=(". ", " = "))
print(news_json)