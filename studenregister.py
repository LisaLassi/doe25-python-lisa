menu_is_running = True

studenregister = []

while menu_is_running:
    student = {'Förnamn': '', 'Efternamn': '', 'Ålder': ''}
    menu_choice = input('Gör ett menyval \n[1] LÄGG TILL STUDENT \n[2] LISTA ALLA STUDENTER \n[3] AVSLUTA \n Ditt val:')

    if menu_choice == '1':
        print('Du valde att lägga till en student, ange förnamn & efternamn: ')
        student['Förnamn'] = input('Ange förnamn: ')
        student['Efternamn'] = input('Ange efternamn: ')
        student['Ålder'] = input('Ange ålder: ')
        
        studenregister.append(student)
    
        print('Studenten är tillagd! \n')
        
    elif menu_choice == '2':
        print('Du valde att lista alla studenter: ')
        print(studenregister)
        print('\n')
        
    elif menu_choice == '3':
        print('Avslutar programmet...')
        break