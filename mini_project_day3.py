#tworzenie listy filmow i ich ocen

filmy = {}

for i in range(3):
    tytul = input("Podaj tytuł filmu: ")
    ocena = input("podaj ocene tego filmu: ")
    filmy[tytul] = ocena 

print("lista wszystkich filmów")
for tytul, ocena in filmy.items():
    print(f"Film: {tytul} - ocena: {ocena}")

#wyswietlanie jesli ocena jest wieksza niz xyz
print("Filmy z ocenami powyzej 6")
for tytul, ocene in filmy.items():
    if ocena > "7":
        print(f"Film: {tytul} - ocena: {ocena}")


        
