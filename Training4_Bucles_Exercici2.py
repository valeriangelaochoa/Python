Notes = [0,1,2,3,4,5,6,7,8,9,10,-1]
for nota in Notes:
    if nota > -1:
        print(nota)
    if nota == -1:
        print(nota)
        break
if max(Notes) == 10:
    print("Hi ha hagut alguna nota que té un 10")
else:
    print("No hi ha cap 10")