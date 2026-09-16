import mysql.connector

def hae_lentokenttien_maarat(maakoodi):
    sql = """
        SELECT type, COUNT(*) AS lukumaara
        FROM airport
        WHERE iso_country = %s
        GROUP BY type
        ORDER BY lukumaara DESC
    """
    kursori = yhteys.cursor()
    kursori.execute(sql, (maakoodi,))
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        print(f"Lentokentät maassa {maakoodi}:")
        for rivi in tulos:
            print(f"{rivi[0]}: {rivi[1]} kappaletta")
    else:
        print("Lentokenttiä ei löytynyt annetulla maakoodilla.")

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='student',
    password='student123',
    autocommit=True
)

maakoodi = input("Anna maakoodi (esim. FI): ")
hae_lentokenttien_maarat(maakoodi)

yhteys.close()