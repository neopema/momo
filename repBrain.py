import os.path
import os


from lettering import first_hello, first_welcome

PATH = './user_profile/'

def firstRun():
    if os.path.exists(PATH) == False: return True

    return False


def reptilian_init():
    first_welcome()

    name = input('Como quiere que te llame?: ')
    birthday = input('Cumpleanos (XD) en formato DD/MM: ')
    person = input('La persona que mas te importa (ademas de ti mismo): ')

    # proximos: una frase, algo que te guste mucho

    first_hello(name)

    os.makedirs('user_profile')
    with open(PATH+'user.txt', "w+",  encoding='utf-8') as f:
        f.write(name)
        f.write('/n')
        f.write(birthday)
        f.write('/n')
        f.write(person)
        f.write('/n')

    input("Configuracion finalizada! Presione cualquier tecla para continuar...")