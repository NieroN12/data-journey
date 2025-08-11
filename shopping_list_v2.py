shopping_list = []  #rozpoczecie kodu

#pytanko o produkty
product1 = input("Podaj pierwszy produkt")
product2 = input("Podaj drugi produkt")
product3 = input("Podaj trzeci produkt")

# Dodajemy do listy
shopping_list.append(product1)
shopping_list.append(product2)
shopping_list.append(product3)

#wyswietlamy liste, ale od konca bo czemu nie
print("Twoja lista zakupów od końca, bo czemu nie? :", shopping_list[::-1])
