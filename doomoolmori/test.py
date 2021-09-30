import requests

ticker = "AAPL"
url = f"https://rest.yahoofinanceapi.com/v8/finance/chart/{ticker}"

querystring = {"range":"1mo", "interval":"1d"}

headers = {
    'x-api-key': "GLlnqxSQh372hIBoSLMIj9S9fH2rSPOs7XjaVolf"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
# GLlnqxSQh372hIBoSLMIj9S9fH2rSPOs7XjaVolf