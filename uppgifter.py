# 1. Variabler och datatyper
'''
# a) Skapa variablerna name(str), age(int), height(float)
# b) Skriv ut variablerna med print()
name = input("Vad heter du?: ")
age = int(input("Hur gammal är du?: "))
height = float(input("Hur lång är du (i meter)?: "))
print(f"Hej {name} som är {age} år gammal och {height} meter lång!")

# c) använd type() för att ta reda på datatyperna
print(type(name))
print(type(age))
print(type(height))
'''

# 2. Input och utskrift
# a) Fråga användaren om deras favoritfärg och skriv ut ett svar
''' 
favorite_color = input("Vad är din favorit färg? ")
print("Min favorit färg är också " + favorite_color + "!")
'''

# b) Fråga användaren om två tal och skriv ut summan
'''
print("Var god och ange två tal:")
num1 = input("Tal 1: ")
num2 = input("Tal 2: ")
sum = int(num1) + int(num2) 
print("Summan av dina valda tal är: " + str(sum) + "!")
print(f"Summan av dina valda tal är: {sum}!")  # Alternativ med f-string, där jag inte behöver formatera om sum till en sträng.
'''
# c) Testa att skriva ut med f-strängar
# Se ovan i 1 b) & 2 b).

# 3. Strängformatering
# a) Skapa en sträng som säger "Mitt namn är ... och jag är ... år" med variabler.
'''
name = "Lisa"
age = 27
print(f"Mitt namn är {name} och jag är {age} år.")
'''

# b) Låt användaren skriva in en mening och skriv ut den i versaler (upper())
'''
sentence = input("Skriv en mening: ")
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())

# c) Ta reda på längden av en sträng med len()
print(f"Din mening är {len(sentence)} tecken långt.")
'''

# 4. Loopar & villkor
# a) Skriv en loop som skriver talen 1 till 10
'''
for i in range(1, 11): # Start på 1, slutar innan 11
    print(i)
'''
# b) Skriv en loop som räknar ner från 5 till 1 och sedan skriver "Klar!"
'''
for i in range(5, 0, -1): # Start på 5, slutar innan 0, räknar ner med -1
    print (i)
print("Klar!")
'''

# c) Fråga användaren om deras ålder och skriv ut om de är minderåriga eller myndiga
'''
age = input("Hur gammal är du?: ")
if int(age) < 18:
    print("Du är minderårig!")
elif int(age) >= 18:
    print("Du är myndig!")
'''

# 5. Listor
# a) Skapa en lista med 3 favoritfrukter
fruits = ["melon", "mango", "banan"]
print(*fruits, sep = ', ')

''' #ska skriva ut användarens inmatade frukter
print(f"Dina favoritfrukter är: {fruits[0], fruits[1]} och {fruits[2]} !")
'''
# b) Lägg till en frukt i listan med append()
fruits.append("dragonfruit")
print(*fruits, sep = ', ')

# c) Skriv ut endast den första och sista frukten i listan.
print(f"Den första frukten i listan är: {fruits[0]} och den sista frukten är: {fruits[-1]}") # -1 för att komma åt sista elementet i listan (-1 är alltid sista elementet i en lista)

# 6. Dictionaries

# 7. Mini-projekt: Kombinera