menu_is_running = True

studenregister = []

while menu_is_running:

    print("\nGör ett menyval:")
    print("[1] Lägg till student")
    print("[2] Lista alla studenter")
    print("[3] Sök efter en student")
    print("[4] Räkna genomsnittlig ålder")
    print("[5] Ta bort student")
    print("[6] Avsluta")

    try:
        menu_choice = int(input("Ditt val: "))
        if menu_choice < 1 or menu_choice > 6:
            print("❌ OUPS! Du måste skriva en siffra mellan 1-6.")
            continue
    except ValueError:
        print("❌ Ogiltigt val! Du måste ange en siffra (1-6).")
        continue
        
    if menu_choice == 1:
        print('\n---Du valde att lägga till en student--- ')

        while True:
            name = input('\n• Ange förnamn: ')
            if name.isalpha():
                break
            else:
                print('❌ Ogiltigt namn! Namnet får endast innehålla bokstäver. Försök igen.\n')
            
        while True:
            lastname = input('• Ange efternamn: ')
            if lastname.isalpha():
                break
            else:
                print('❌ Ogiltigt efternamn! Efternamnet får endast innehålla bokstäver. Försök igen.\n')

        while True:
            age = input('• Ange ålder: ')
            if age.isdigit() and 0 < int(age) < 120:
                break
            else:
                print('❌ Ogiltig ålder! Åldern måste vara ett tal mellan 1-119. Försök igen.\n')
            

        student = {
        'Förnamn' : str(name), 
        'Efternamn': str(lastname),
        'Ålder': int(age)
        }
        
        studenregister.append(student)
    
        print('\n-Studenten är tillagd- \n')
        input('Tryck på Enter för att återgå till menyn...')
        
    elif menu_choice == 2:
        print('\n---- Du valde att lista alla studenter ---- ')
        count = 0
    
        if len(studenregister) == 0:
          print('\nDet finns inga studenter i registret.')
        
        else:
            for i in studenregister:
             count += 1
             print(f'{count}. {i["Förnamn"]} {i["Efternamn"]} • {i["Ålder"]} år')
        print('')

        input('Tryck på Enter för att återgå till menyn...')

    elif menu_choice == 3:
        print('\nDu valde att söka efter en student')
        search_name = input('Ange förnamn på studenten du söker: ')

        found = False
        count = 0
        for student in studenregister:
            if student['Förnamn'] == search_name:
                count += 1
                print(f'\n------ Student {count} ------')
                print(f'Namn: {student["Förnamn"]} {student["Efternamn"]}, Ålder: {student["Ålder"]} år')
                found = True
            
        if not found:
            print(f'\nStudenten {search_name} finns inte i registret.')

        else:
            print(f'\n• Hittade {count} studenter med namnet {search_name} •')
            input('\nTryck på Enter för att återgå till menyn...')

    elif menu_choice == 4:
        print('\nDu valde att räkna ut genomsnittlig ålder')
        if len(studenregister) == 0:
            print('Inga studenter i registret.')
        else:
            total_age = 0
            for student in studenregister:
                total_age = total_age + int(student['Ålder'])
            average_age = total_age / len(studenregister)
            print(f'\nDen genomsnittliga åldern är: {average_age} år')
        print('')
        input('Tryck på Enter för att återgå till menyn...')

    elif menu_choice == 5:
        print('\nDu valde att ta bort en student')
        remove_name = input('Ange förnamn på studenten du vill ta bort: ')
        for student in studenregister:
            if student['Förnamn'] == remove_name:
                studenregister.remove(student)
                print(f'- Studenten {remove_name} är borttagen från registret -')
                break
            else:
                print(f'\n• Studenten {remove_name} finns inte i registret.')
        print('')
        input('Tryck på Enter för att återgå till menyn...')
        
    elif menu_choice == 6:
        print('Avslutar programmet...')
        break