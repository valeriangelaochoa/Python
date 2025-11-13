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