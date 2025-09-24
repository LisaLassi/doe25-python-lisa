menu_is_running = True

while menu_is_running:
    menu_choice = input('Gör ett menyval \n[1] LÄGG TILL STUDENT \n[2] LISTA ALLA STUDENTER \n[3] AVSLUTA \n Ditt val:')
        
    if menu_choice == '1':
        print('Du valde att lägga till en student, ange förnamn & efternamn: ')
        name = input('Förnamn: ')
        lastname = input('Efternamn: ')
        age = input('Ålder: ')

        studenregister ={
        'Förnamn' : {name},
        'Efternamn' : {lastname},
        'Ålder' : {age}
        }

    elif menu_choice == '2': #måste komma åt alla värden i dictionaryn
        print('Du valde att lista alla studenter: \n')
        for värde in studenregister:
            print(värde, ":", studenregister[värde])

        #print('Du valde att lista alla studenter: \n' (studenregister))

    elif menu_choice == '3':
        print('Avslutar programmet...')
        break