# tworzenie listy i słowników
person = {
    "name": "Anna",
    "age": 29,
    "city": "Warszawa"
}
print(person["name"])  # wyświetli: Anna

person = {
    "imie": "Heniek",
    "age": 14,
    "city": "Warszawa"
}
print(person["city"]) 

person = {
    "jabłko": 2.5 ,
    "chleb": 3.5 ,
    "jajko": 1.5 
}
print(person["jajko"])

#tworzenie krotek/tupli

coordinates = (5,60)
print(coordinates[1])

#tworzenie pętli for & while

fruits = ["jabłko", "banan", "wiśnia"]
for fruit in fruits:
    print(fruit)

count = 0
while count < 3:
    print(count)
    count += 1

count = 0
while count < 10:
    print(count)
    count += 2

for fruit in person:
    print(print(f"Owoc: {fruit}, cena: {person[fruit]} zł"))    


#instrukcje warunkowe

age = int(input("ile masz lat? "))
if age < 18:
    print("jesteś niepełnoletni/a")
elif age < 65:
    print("jesteś dorosły")
else:
    print("jesteś seniorem")

#lista zakupow

num_products = int(input("ile produktów chcesz dodać? "))

for i in range(num_products):
    name = input("Podaj nazwę produktu: ")
    price = float(input("Podaj cenę produktu: "))
    if price > 5:
        print("Drogi produkt")
    else:
        print("Produkt w normalnej cenie")

