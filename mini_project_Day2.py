#zapytanie o liczbe
num_product = int(input("ile produktów chcesz dodać? "))
#koszyk
produkty = {}

for i in range(num_product):   
    name = input(f"Podaj nazwę produktu #{i+1}: ")
    price = float(input(f"Podaj cenę produktu '{name}': "))
    produkty[name] = price

#wyswietlanie
print("/nLista zakupów:")
for name,price in produkty.items():
    print(f"{name} - {price} zł")

#lista drogich produktów
print("/nDrogie produkty (>5 zł): ")
for name, price in produkty.items():
    if price > 5:
        print(f"{name} = {price} zł")

#całkowity koszt
total = sum(produkty.values())
print(f"/nCałkowity koszt zakupów: {total} zł")
