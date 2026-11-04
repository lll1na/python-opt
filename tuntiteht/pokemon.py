import requests

def hae_pokemon(nimi):
    url = f"https://pokeapi.co/api/v2/pokemon/{nimi.lower()}"

    try:
        vastaus = requests.get(url)

        if vastaus.status_code == 200:
            data = vastaus.json()

            tyypit = [
                tyyppi["type"]["name"]
                for tyyppi in data["types"]
            ]

            print(f"Pokémon: {data['name'].capitalize()}")
            print("Tyypit:", ", ".join(tyypit))

        elif vastaus.status_code == 404:
            print("Pokémonia ei löytynyt.")

        else:
            print("Virhe palvelimella.")

    except requests.exceptions.RequestException:
        print("Yhteysvirhe. Tarkista internet-yhteys.")


nimi = input("Anna Pokémonin nimi: ")
hae_pokemon(nimi)