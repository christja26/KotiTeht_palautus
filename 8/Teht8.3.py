import mysql.connector
from geopy import distance
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='juuri',
         autocommit=True
         )
annettu = input("anna lentoasema ICAO koodi: ")
annettu_toka = input("anna toinen lentoasema ICAO koodi: ")
sql = f" select latitude_deg, longitude_deg from airport where ident='{annettu.upper()}' or ident='{annettu_toka.upper()}';'"
kursori = yhteys.cursor()
kursori.execute(sql)
kysely_vastaus = kursori.fetchall()
print(f"{distance.distance(kysely_vastaus[0],kysely_vastaus[1]).km:.2f}km on etäisyys annetuista asemista.")