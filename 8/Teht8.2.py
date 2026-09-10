import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='juuri',
         autocommit=True
         )
maakoodi = input("anna maakoodi: ")
pienet_asemat = 0
keskikokoiset_asemat = 0
suuret_asemat = 0
heli_asemat = 0
sql = f"select type from airport where iso_country='{maakoodi}';"
kursori = yhteys.cursor()
kursori.execute(sql)
kysely_vastaus = kursori.fetchall()
for vastaus in kysely_vastaus:
    for teksti in vastaus:
        if teksti == "small_airport":
            pienet_asemat += 1
        elif teksti == "large_airport":
            suuret_asemat += 1
        elif teksti == "medium_airport":
            keskikokoiset_asemat += 1
        elif teksti == "heliport":
            heli_asemat += 1
print(f"pienet asemat: {pienet_asemat}\nkeskikokoiset asemat: {keskikokoiset_asemat}\nsuuret asemat: {suuret_asemat}\nhelikopterikenttiä: {heli_asemat}")








