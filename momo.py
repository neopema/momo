from ast import arg
import sys

from uftools import clear
from momoCli import execute
from repBrain import firstRun, reptilian_init
from primmaryCommands import check_command, exit_command
from lettering import default_welcome, default_command_line


def default_command_handler():
    current_command = default_command_line()
    if current_command == "exit": return exit_command()

    execute(current_command)
    default_command_handler()


def default_execution():
    clear()
    default_welcome()
    #default_command_handler()


def command_execution(args_params):
    #verificamos los argumentos
    args_list = []
    main_command = ""

    for i, arg in enumerate(args_params):
        if i == 0:
            continue
        if i == 1:
            main_command = arg  
            continue

        args_list.append(arg)

    valid_main_command = check_command(main_command)

    #argumentos invalidos
    if valid_main_command[1] == False:
        print(valid_main_command[0])

        return

    #argumentos validos
    print(f"{main_command} ejecutado")
    print(f"arguments: {args_list}")

    default_welcome()
    default_command_handler()


def first_execution():
    reptilian_init()
    
    return default_execution()


def run():
    #first run
    if firstRun(): return first_execution()

    #arguments start
    arguments = sys.argv
    if len(arguments) > 2 : return command_execution(arguments)
    
    #default start
    default_execution()


if __name__ == '__main__':
    run()