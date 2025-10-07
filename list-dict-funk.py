# LISTOR
# 1.Summera tal: Skapa en lista med heltal. Använd en for-loop för att summera alla tal och skriv ut summan.
heltal_lista = [5, 10, 15, 20, 25, 30]
sum = 0 # Initiera en variabel för att lagra summan
for tal in heltal_lista: # Gå igenom varje tal i listan med en for-loop
    sum = sum + tal # Lägg till det aktuella talet till summan
print(f"Summan av alla tal i listan är: {sum}\n") # Skriv ut den totala summan

# 2. Största talet: Skriv ett program som går igenom en lista med heltal och hittar det största talet.
största_talet = max(heltal_lista)
print(f"Det största talet i listan är: {största_talet}\n")

# 3. Multiplikationstabeller: Låt användaren skriva in ett tal. Skriv sedan ut multiplikationstabellen för det talet (1–10).
user_number = input("Ange ett heltal: ")
talet = int(user_number) # Om jag inte koverterar om str till int så skrivs bara siffran ut x talet, t ex 4x3 = 444, 4x5 = 44444
for i in range(1, 11):
    produkt = talet * i
    print(f"{talet} x {i} = {produkt}")
print("\n")

# 4. Filtrera jämna tal: Skapa en lista med tal 1–20. Använd en loop för att skriva ut bara de jämna talen.
min_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for num in min_lista:
    if num % 2 == 0:
        print(num, end= ' , ') # Gör så att talen skrivs ut på en rad istället för ny rad för varje siffra
print("\n")

# 5. Vänd på en lista: Skriv en loop som skriver ut en lista baklänges, utan att använda reversed() eller slicing.
ny_lista = [1, 2, 3, 4, 5]
for i in range(len(ny_lista) -1, -1, -1):
    print(ny_lista[i])
    
'''
Första -1 är det sista indexet i listan.
Andra -1 är det andra stoppvärdet, vilket betyder att loopen går fram till index 0.
Tredje -1 är stegvärdet, som gör att vi går bakåt.
'''

#DICTIONARIES
# 1. Skapa en användarprofil: Skapa en dictionary med nycklarna namn, ålder, stad. Skriv ut dictionaryn.
my_dict = {
    "namn" : "Lisa",
    "ålder" : 27,
    "stad" : "Stockholm"
}

print(my_dict)

# 2. Uppdatera profil: Låt användaren skriva in en favoritfärg och lägg till den i dictionaryn.
my_dict["färg"] = input("Vad är din favoritfärg?: ") #Lägger till ett nytt nyckelvärde-par
print(my_dict)

# 3. Telefonbok: Skapa en dictionary där namn är nyckel och telefonnummer är värde. Låt användaren slå upp en person.
telefonbok = {
    "Lisa" : "12345",
    "Ior" : "678910",
    "Tove" : "111213",
    "Helene" : "141516"
}

search = input("Ange förnamn på den du söker: ")
for person in telefonbok:
    if person == search:
        print(f"Numret till {search} är {telefonbok[search]}")

# 4. Ordfrekvens: Låt användaren skriva in en mening. Gör en dictionary där varje ord är nyckel och antalet förekomster är värdet.

# 5. Inventarielista: Skapa en dictionary med varor och deras antal. Gör ett menyval:
#○ Visa alla varor
#○ Lägg till en vara
#○ Ändra antal på en vara

inventering = {
    "banan" : "25",
    "äpple" : "10",
    "päron" : "35",
    "apelsin" : "20",
    "vattenmelon" : "40"
}
while True:
    print("MENY")
    print("(1) Visa alla varor")
    print("(2) Lägg till en vara")
    print("(3) Ändra antalet på en vara")
    print("(4) Avsluta")
    menyval = input("Välj: ")
    if menyval == "1":
        print("Här är alla varor: ")
        print(inventering)

    elif menyval == "2":
        tillägg = input("Vad vill du lägga till?: ")
        antal = input(f"Hur många av {tillägg} vill du lägga till: ")
        inventering[tillägg] = antal

        print(inventering)

    elif menyval == "3":
        ändring = input("Vilken vara vill du ändra antalet på?: ")
        nytt_antal = input(f"Hur många av {ändring} ska det vara: ")
        if ändring in inventering:
            inventering[ändring] = nytt_antal
            print(inventering)
        else:
            print("Varan hittades inte")

    elif menyval == "4":
        break

# FUNKTIONER
# 1. Kvadrat: Skriv en funktion square(x) som returnerar kvadraten av ett tal.
def square(x):
    return x ** x

tal = int(input("Ange ett tal: "))
resultat = square(tal)
print(resultat)

# 2. Max av två: Skriv en funktion maximum(a, b) som returnerar det största av två tal.
def maximmum(a, b):
    return max(a, b)

tal1 = int(input("Ange tal 1: "))
tal2 = int(input("Ange tal 2: "))

resultat2 = max(tal1, tal2)
print(f"Det största talet är: {resultat2}!")

# 3. Medelvärde: Skriv en funktion average(numbers) som tar en lista med tal och returnerar medelvärdet.
def average(numbers):
    return sum(numbers) / len(numbers)

min_lista = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print("Medelvärdet av listan är ", average(min_lista))

# 4. Palindromtest: Skriv en funktion som returnerar True om ordet är samma fram- och baklänges.

# 5. Multiplikationstabell som funktion: Skriv en funktion multiplikation_table(n) som skriver ut multiplikationstabellen för ett tal.
def multiplikation_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n * i}")

talet = int(input("Ange ett tal: "))
multiplikation_table(talet)