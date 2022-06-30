from repBrain import firstRun, reptilian_init
from primmaryCommands import check_command, exit_command
from commandLineManager import execute
from lettering import default_welcome, default_command_line
from uftools import clear

import sys

def default_command_handler():
    current_command = default_command_line()
    if current_command == "exit": return exit_command()

    execute(current_command)
    default_command_handler()


def default_execution():
    clear()
    default_welcome()
    default_command_handler()


def command_execution(args_params):
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

    if valid_main_command[1] == False:
        print(valid_main_command[0])

        return

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

    #reading arguments
    argumentos = sys.argv
    largo = len(argumentos)

    #default start
    if largo < 2 : return default_execution()
    
    #arguments start
    command_execution(argumentos)


if __name__ == '__main__':
    run()