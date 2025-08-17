#pętle i logika
for i in range(1,11):
    if i % 2 == 0:
        print (i)

#zadanko
for i in range(3):
    haslo = input("Jakie jest hasło? ")
    if haslo == "python":
        print("hasło poprawne")
        break
    else:  
        print("hasło nie poprawne")

#uzycie while
haslo = ""

while haslo != "python":
    haslo = input("Jakie jest hasło? ")
    if haslo == "python":
        print("Hasło poprawne ")
    else:
        print("Hasło niepoprawne, spróbuj ponownie.")


#continue i brak

for a in range(11, 21):
    if a == 18:
        break
    if a % 3 == 0:
        continue
    print(a)

#elif etc
w = int(input("Ile masz lat?"))
if w < 18:
   print("Jesteś niepełnoletni ")
elif w in range (18,65):
    print("jesteś pełnoletni")
else:
    print("Senior" )
