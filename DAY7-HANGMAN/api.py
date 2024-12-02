import requests
import random
num = random.randint(3,5)

url = f"https://random-word-api.herokuapp.com/word?length={num}"
try:
    response = requests.get(url)

    response.raise_for_status()
    data = response.json()
except requests.exceptions.HTTPError as errh:
    print("HTTP Error")
    print(errh.args[0])