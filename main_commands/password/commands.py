from ast import arg
import generate


def new_password(argumentos):

    lenght = 16
    schars = True
    title = ""
    print("Bienvenido al generador de contrasenas de Momo\n")

    if argumentos == []:
        title = generate.title()
        lenght = generate.lenght()
        schars = generate.symbols()
    else:
        title = argumentos[0]
        lenght = argumentos[1]
        schars = arg
    

   

    print("\n\nGenerando contrasena")

    
    


