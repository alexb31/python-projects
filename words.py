import requests

url = "https://www.randomlists.com/data/words.json"

response = requests.get(url)

def get_words():
    if response.status_code == 200:
        data = response.json()
        return data.get("data", [])

    else:
        print("Error:", response.status_code)
        data = []