import time
from uftools import clear

commands = [
    ['menu', 'm'],
    ['open', 'o'],
    ['run', 'r'],
    ['get', 'g']
]

command_basic_responses = [
    "' no existe o no es ejecutable. Revise la sintaxis y su cabeza.",
    "' es correcto"
]

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
    time.sleep(0.3)
    clear()
