import requests

API_KEY = "LIITÄ_TÄHÄN_OMA_API_AVAIMESI"

paikkakunta = input("Anna paikkakunnan nimi: ")

pyynto = "https://api.openweathermap.org/data/2.5/weather"
parametrit = {
    "q": paikkakunta,
    "appid": API_KEY,
    "lang": "fi", 
}

try:
    vastaus = requests.get(pyynto, params=parametrit, timeout=10)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        saateksti = json_vastaus["weather"][0]["description"]
        kelvin = json_vastaus["main"]["temp"]
        celsius = kelvin - 273.15
        print(f"Säätila: {saateksti}")
        print(f"Lämpötila: {celsius:.1f} °C")
    elif vastaus.status_code == 404:
        print("Paikkakuntaa ei löytynyt.")
    elif vastaus.status_code == 401:
        print("Virheellinen API-avain.")
    else:
        print(f"Virhe: palvelin vastasi koodilla {vastaus.status_code}")
except requests.exceptions.RequestException as e:
    print("Pyyntöä ei voitu suorittaa:", e)