# Funktion för att printa main menyn
def print_main_menu():
    print("\nGör ett menyval:")
    print("[1] Lägg till student")
    print("[2] Lista alla studenter")
    print("[3] Sök efter en student")
    print("[4] Räkna genomsnittlig ålder")
    print("[5] Ta bort student")
    print("[6] Avsluta")

# Funktion för att få ett giltigt för- och efternamn (endast bokstäver)
def get_valid_name(prompt):
    while True:
        name = input(prompt)
        if name.isalpha():
            return name
        else:
            print('- ❌ Ogiltigt namn - Namn får endast innehålla bokstäver. Försök igen')

# Funktion för att få en giltig ålder (positivt heltal)
def get_valid_age(prompt):
    while True:
        age = input(prompt)
        if age.isdigit() and int(age) > 0:
            return int(age)
        else:
            print('- ❌ Ogiltig ålder - Åldern måste vara ett heltal. Försök igen')