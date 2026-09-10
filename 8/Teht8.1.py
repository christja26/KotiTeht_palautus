import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='juuri',
         autocommit=True
         )
annettu = input("anna lentoasema ICAO koodi: ")
sql = f" select name, municipality from airport where ident='{annettu.upper()}';'"
kursori = yhteys.cursor()
kursori.execute(sql)
kysely_vastaus = kursori.fetchall()
print(f"annetun lentokentän nimi on: {kysely_vastaus[0][0]}")
print(f"annetun lentokentän sijaintikunta on: {kysely_vastaus[0][1]}")
