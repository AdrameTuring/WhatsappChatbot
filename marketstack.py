import requests
import os
import json

#API_KEY=os.environ.get("MARKETSTACK_KEY")
BASE_URL="http://api.marketstack.com/v1/"

#Function wich return the latest price for a specific symbol
def get_stock_price(symbol):
    params={
        'access_key':'7d906485b9deab22c8e09e8ad9e3d86a'
    }
    endpoint=''.join([BASE_URL,"tickers/",symbol,"/intraday/latest"])
    api_result=requests.get(endpoint,params)
    api_result_json=json.loads(api_result.text)

    return {
        'last_price':api_result_json["last"]
    }

sortie=get_stock_price("AAPL")
print(sortie)
