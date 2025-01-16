import math
Kokonaisluku1_int= int(input("kokonaisluku 1") )
Kokonaisluku2_int= int(input("kokonaisluku 2") )
Kokonaisluku3_int= int( input("kokonaisluku 3 ") )
summa_int = Kokonaisluku2_int + Kokonaisluku1_int + Kokonaisluku3_int
tulo_int = Kokonaisluku1_int * Kokonaisluku2_int * Kokonaisluku3_int
keskiarvo_float = float( Kokonaisluku1_int+ Kokonaisluku2_int + Kokonaisluku3_int / 3)
x= round(keskiarvo_float, 2)
print(f"Kokonaisluku summa = {summa_int}")
print(f"Kokonaisluku tulo = {tulo_int}")
print(f" Kokonaisluku keskiarvo = {x}")



