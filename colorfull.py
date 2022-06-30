from colorama import init, Fore, Back, Style

init()

TITLES_FORES = [Fore.WHITE, Fore.WHITE, Fore.CYAN, Fore.CYAN, Fore.MAGENTA, Fore.MAGENTA, Fore.MAGENTA, Fore.WHITE, Fore.WHITE, Fore.CYAN, Fore.CYAN, Fore.MAGENTA, Fore.MAGENTA, Fore.MAGENTA]

FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]

BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]

BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]


def print_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    """Wrap en print() para color y brillo"""
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)

def input_momo(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    """Wrap en input() para color y brillo"""
    temp = input(f"{brightness}{BACKS[5]}{FORES[7]}{s}{BRIGHTNESS[2]}{BACKS[0]}{FORES[7]} ", **kwargs)
    return temp
