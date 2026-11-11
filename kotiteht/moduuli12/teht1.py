import requests

pyynto = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(pyynto, timeout=10)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(json_vastaus["value"])
    else:
        print(f"Virhe: palvelin vastasi koodilla {vastaus.status_code}")
except requests.exceptions.RequestException as e:
    print("Pyyntöä ei voitu suorittaa:", e)