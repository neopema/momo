from commands import check_command, exit_command
from command_manager import execute
from lettering import default_welcome, default_command_line

import sys

def default_command_handler():
    current_command = default_command_line()
    if current_command == "exit": return exit_command()

    execute(current_command)
    default_command_handler()

def default_execution():
    default_welcome()
    default_command_handler()

def command_execution(args_params):
    args_list = []

    for i, arg in enumerate(args_params):
        if i == 0:
            continue     
        args_list.append(arg)

    main_command = args_list[0]
    valid_main_command = check_command(main_command)

    if valid_main_command[1] == False:
        print(valid_main_command[0])

        return

    print(main_command) 

def run():
    argumentos = sys.argv
    largo = len(argumentos)

    if largo < 2 : return default_execution()
    
    command_execution(argumentos)   

if __name__ == '__main__':
    run()