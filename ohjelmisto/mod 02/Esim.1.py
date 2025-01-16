nimi= "Deni"
print("moi " + nimi + ", mitä kuuluu?")
print(f"Moi {nimi}, kuinkas nyt menee?")


#käyttäjän syötteen lukeminen
#huom: input lukee kaikki syötteet
# aina merkkijonoina
lukuA_str = input("Anna kokonaisluku: ")
#muunnetaan merkkijono kokonaisluvuiksi
lukuA = int( lukuA_str)
# luen käyttäjän syötteen, lukuna
# huom: +input
lukuB = int( input("Anna tonen luku: ") )
summa = lukuA + lukuB
print(f"Lukujesi summa = {summa}")




