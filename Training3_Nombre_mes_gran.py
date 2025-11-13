Nom1= input("Escriu el primer nombre:")
Nom2= input("Escriu el segon nombre:")
Nom3= input("Escriu el tercer nombre:")
if Nom1 >= Nom2:
    if Nom1 >= Nom3:
        print("El nombre més gran és:", Nom1)
if Nom2 >= Nom1:
    if Nom2 >= Nom3:
        print("El nombre més gran és:", Nom2)
if Nom3 >= Nom1:
    if Nom3 >= Nom2:
        print("El nombre més gran és", Nom3)