import requests


# fetch the result of the API
def quote():
    url = "https://wagon-breaking-bad-quotes.herokuapp.com/v1/quotes"
    call = requests.get(url).json()[0]
    response = f"{call['author']} says : {call['quote']}"
    return response


