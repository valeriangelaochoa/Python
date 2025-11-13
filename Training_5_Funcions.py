def area_costat():
    costat = float(input("Introdueix la mida del costat del quadrat:"))
    area = costat * costat
    print("L'àrea del quadra")

def nombres_enters():
        print("Calcularen la suma, la resta, la multiplicació i la divisió")
        Número1 = float (input("Introdueix el primer número enter:"))
        Número2 = float (input("Introdueix el segon número enter:"))
        suma = Número1 + Número2
        resta = Número1 - Número2
        multiplicació = Número1 * Número2
        divisió = Número1 / Número2
        print ("El resultat de la suma és:", int(suma), "El resultat de la resta és:", int(resta), "El resultat de la multiplicació és", int(multiplicació), "El resultat de la divisió és", int(divisió))
    
def crear_frase():
        print("Introdueix les tres paraules per a crar la frase")
        paraula1 = input("Introdueix la primera paraula")
        paraula2 = input("Introdueix la segona paraula")
        paraula3 = input("Introdueix la tercera paraula")
        Frase_feta = "Llamame a " + paraula1 + " dile que estoy en el " + paraula2 + " i que tengo que hablar de " + paraula3 
        print (Frase_feta)
    
def suma_nombres():
        print("Introduiex dos nombres")
        numero1 = float(input("Introdueix el primer número"))
        numero2 = float(input("Introdueix el segon número"))
        suma = numero1 + numero2
        print("El resultat de la suma és", round(suma))

def majors_edat():
    edat = int(input("escriu la teva edat:"))
    if edat >= 18:
        print("Ets major d'edat")
    else:
        print("Ets menor d'edat")

def nombre_gran():
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

def positiu_o_negatiu():
    Nombre = input("Escriu el nombre que vulguis: ")
    if int(Nombre) >= 0:
        print("Es un nombre positiu")
    else:
        print("Es un nombre negatiu")

def nombre_impars():
    print("Nombres impars entre 1 i 200: ")
    for v in range(1,201):
        if v %2 == 0:
            print(v)

def nombre_10():
    Nota = 0
    flap = 0
    while Nota != -1:
        Nota = int(input("Introdueix un nombre entre 0-10 per a finalitzar: "))
        if Nota ==10:
            flap= 1
    if flap == 1:
        print("Hi ha hagut alguna nota que té un 10")
    else:
        print("No hi ha cap 10")

def nombre_negatiu():
    Notes = [-5,-4,-3,-2,-1,0,1,2,3,4]
    for Nombre in Notes:
        print(Nombre)
    if min(Notes) < 10:
        print("Hi habia almenys un nombre negatiu")
    else:
        print("No hi ha cap nombre negatiu")

def main():
    while True:
        print("Menu")
        print("1. Calcul de l'area d'un quadrat: ")
        print("2. Calculs de dos nombres enters: ")
        print("3. Crea una frase amb tres paraules: ")
        print("4. Suma de dos numeros: ")
        print("5. Ets major d'edat o no: ")
        print("6. Quin es el nombre més gran: ")
        print("7. Es positiu o negatiu: ")
        print("8. Nombres impars del 1 al 200: ")
        print("9. Sequencia de notes: ")
        print("10. Hi ha un nombre negatiu: ")

        opcio = input("Eligeix una opció: ").upper()

        if opcio == "1":
            area_costat()
        elif opcio == "2":
            nombres_enters()
        elif opcio == "3":
            crear_frase()
        elif opcio == "4":
            suma_nombres()
        elif opcio == "5":
            majors_edat()
        elif opcio == "6":
            nombre_gran()
        elif opcio == "7":
            positiu_o_negatiu()
        elif opcio == "8":
            nombre_impars()
        elif opcio == "9":
            nombre_10()
        elif opcio == "10":
            nombre_negatiu()
        elif opcio == "Q":
            print("Tancament del programa....")
            break
        else:
            print("No es reconeix el valor posat. Tornar a intentar.\n")
if __name__=="__main__":
    main()