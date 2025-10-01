menu_is_running = True

studenregister = []

from funk import print_main_menu
from funk import get_valid_name
from funk import get_valid_age

while menu_is_running:
    print_main_menu()

    try:
        menu_choice = int(input("Ditt val: "))
        if menu_choice < 1 or menu_choice > 6:
            print("❌ OUPS! Du måste skriva en siffra mellan 1-6.")
            continue
    except:
        print("❌ Ogiltigt val! Du måste ange en siffra (1-6).")
        continue
        
    if menu_choice == 1:
        print('\n---Du valde att lägga till en student--- ')
        
        name = get_valid_name('\n• Ange förnamn: ')
        lastname = get_valid_name('\n• Ange efternamn: ')
        age = get_valid_age('\n• Ange ålder: ')

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