menu_is_running = True

studenregister = []

while menu_is_running:
    menu_choice = input('Gör ett menyval \n[1] LÄGG TILL STUDENT \n[2] LISTA ALLA STUDENTER \n[3] SÖK EFTER EN STUDENT \n[4] RÄKNA GENOMSNITTLIG ÅLDER \n[5] AVSLUTA \n Ditt val:')

    if menu_choice == '1':
        print('Du valde att lägga till en student, ange förnamn & efternamn: ')
        name = input('Ange förnamn: ')
        lastname = input('Ange efternamn: ')
        age = input('Ange ålder: ')

        student = {
        'Förnamn' : str(name), 
        'Efternamn': str(lastname),
        'Ålder': int(age)
        }
        
        studenregister.append(student)
    
        print('Studenten är tillagd! \n')
        
    elif menu_choice == '2':
        print('Du valde att lista alla studenter: ')
        for i in studenregister[::1]:
            print(f'Student: {i}')
        print('')

    elif menu_choice == '3':
        print('Du valde att söka efter en student')
        search_name = input('Ange förnamn på studenten du söker: ')
        for student in studenregister:
            if student['Förnamn'] == search_name:
                print(f'Studenten {search_name} finns i registret!')
                print(f'Studentens information är:')
                print(student)
            else:
                print(f'Studenten {search_name} finns inte i registret.')

    elif menu_choice == '4':
        print('Du valde att räkna ut genomsnittlig ålder')
        if len(studenregister) == 0:
            print('Inga studenter i registret.')
        else:
            total_age = 0
            for student in studenregister:
                total_age = total_age + int(student['Ålder'])
            average_age = total_age / len(studenregister)
            print(f'Den genomsnittliga åldern är: {average_age} år')
        print('')
        
    elif menu_choice == '5':
        print('Avslutar programmet...')
        break