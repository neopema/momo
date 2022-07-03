import random
from re import L
import string

def generate(symbols: bool = True, lenght: int = 16) -> str:

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    nums = string.digits
    symbols = ""

    if symbols:
        symbols = string.punctuation

    all = lower + upper + nums + symbols

    aux = random.sample(all, lenght)

    new_password = "".join(aux)

    return new_password

def lenght() -> int:
    l = 16

    try:
        l = int(input("Largo de la contrasena (default 16): "))
    except ValueError:
        print("El valor ingresado no es valido o es nulo. Definiendo valor por defecto (16)")

    return l

def symbols() -> bool:
    schars = True
    spchars = input("Desea usar caracteres especiales? (Si por defecto) (y/N): ")

    if spchars == "N" or spchars == "n":
        schars = False

    return schars

def title() -> str: 
    title = input("Titulo del sitio: ")

    return title