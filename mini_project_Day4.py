#
import random

#tworzenie maszyny losujacej
Liczba = random.randint(1,20)
for Liczba in range(3):         
    guess=int(input("zgadnij liczbe od 1 do 20: "))
#warunki
    if Liczba == guess:
        print("brawo")
        break
    elif Liczba < guess:
        print("Za dużo...")
    else:
        print("Za mało...")
else:
    print(f"beka z cb, to było {Liczba}")