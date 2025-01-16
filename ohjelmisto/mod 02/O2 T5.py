Leiviskä_float = float(input("anna leiviska "))
Naula_float = float(input("anna naula "))
Luoti_float = float(input("anna luoti "))

Leiviskä_G = Leiviskä_float*20*32*13.3
Naula_g = Naula_float*32*13.3
Luoti_g = Luoti_float*13.3

Grammojen_tulo = Leiviskä_G + Naula_g + Luoti_g

Kilo_g = int(Grammojen_tulo // 1000)
G = round(float(Grammojen_tulo - Kilo_g * 1000), 2)

print(f"Kilogrammat: {Kilo_g}")
print(f"Grammat: {G}")

