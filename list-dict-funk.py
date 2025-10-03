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
# FUNKTIONER