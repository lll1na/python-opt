import mysql.connector

def hae_lentokentta(icao_koodi):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao_koodi,))
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän nimi: {rivi[0]}")
            print(f"Sijaintikunta: {rivi[1]}")
    else:
        print("Lentokenttää ei löytynyt annetulla ICAO-koodilla.")

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='student',
    password='student123',
    autocommit=True
)

icao_koodi = input("Anna lentoaseman ICAO-koodi: ")
hae_lentokentta(icao_koodi)

yhteys.close()