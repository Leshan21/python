import requests
import hangman

word = hangman.winnig_string

url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

response = requests.get(url)

if response.status_code == 200:
    
    json_data = response.json()
    
    
    try:
        
        first_entry = json_data[0]  
        first_meaning = first_entry["meanings"][0]  
        first_definition = first_meaning["definitions"][0]["definition"]  

    except (IndexError, KeyError) as e:
        print("Error navigating the JSON structure:", e)
else:
    print(f"Failed to fetch data. HTTP Status: {response.status_code}")
