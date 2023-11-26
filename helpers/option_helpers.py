from os import system
from config.data import selections 


def menu(options, section) -> int:
    
    list_options = options[section]['options']
    
    show_options(options, list_options, section)
    option = get_option(list_options)
    return option
    
    
    
def show_options(options, list_options, section) -> None:
    
    system('cls')
    print(options[section]['question'], '\n')
    
    for index, option in enumerate(list_options):
        number = index + 1
        print(f'{number} - {option}')
    print('0 - Salir\n')
    
  
    
def get_option(list_options):
    
    valid_option = False
    
    while not valid_option:
        selection = input('Ingrese su opción: ')
        valid_option = validate_option(selection, list_options)
    
    return int(selection)



def validate_option(selection, list_options):
    
    try:
        selection = int(selection)
        
        if selection == 0:
            exit()
            
        if(selection < 0 or selection > len(list_options)):
            print('Opcion inválida. Ingrese una opción válida.\n')
            return False
        
    except ValueError:
        print('Ingrese únicamente números.\n')
        return False
    
    return True



