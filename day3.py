#ćwicenie podstawowych zagadnień i komend

zakupy = ["piła", "piłka", "klątwa", "prom", "złom"]

zakupy.append("ziom"),
zakupy.remove("piła")
zakupy.pop(2)

print(len(zakupy), zakupy)

#dalej nauka, tuple, próba zmian   

komoda = tuple["3", "4", "5"]

#komoda.append["kebab"] nie dziala

print(komoda)

#lista, dodawanie, odejmowanie i wyswietlanie

Kaczki = {
    "Szara": 2,
    "Czarna": 3,
    "biała": 1
}

Kaczki["Czerwone"] = 3
del Kaczki["biała"]
print(Kaczki)

print(Kaczki.keys(), Kaczki.values())

#zbiory

cyferki = {"jeden", "dwa", "trzy"}

cyferki.add("cztery")
cyferki.remove("dwa")
cyferki.discard("jed")

print(cyferki)

#zbiory, porównanie komend
A = {"a", "b", "c"}
B = {"d", "b", "f"}

print(A | B)

print(A.intersection(B))

print(A.difference(B))









