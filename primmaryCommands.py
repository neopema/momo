from cgitb import text
import time
from uftools import clear
from main_commands.password.commands import new

commands = [
    ['menu', 'm'],
    ['open', 'o'],
    ['run', 'r'],
    ['get', 'g'],
    ['cli', 'c'],
    ['pass', 'p']
]

command_basic_responses = [
    "' no existe o no es ejecutable. Revise la sintaxis y su cabeza.",
    "' es correcto"
]

def execute_primary_command(command: str, arguments: str):
    
    match command:
        case 'pass' | 'p':
            pass


def command_basic_response(result, command):
    result_res = [ False, True ]

    return [
        "El comando '" + command + command_basic_responses[result],
        result_res[result]
    ]

def check_command(command):
    result = 0

    for command_group in commands:
        for command_variation in command_group:
            if command_variation == command:
                result = 1
                break

    return command_basic_response(result, command)

def exit_command():
    time.sleep(0.1)
    clear()
    print('bye bye!')
    time.sleep(0.5)
    clear()
