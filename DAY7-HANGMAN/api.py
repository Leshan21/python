import requests
import random
num = random.randint(5,10)

url = f"https://random-word-api.herokuapp.com/word?length={num}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print(f"Faild to fetch data. Status code: {response.status_code}")    