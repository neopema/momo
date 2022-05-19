from colorama import init, Fore, Back, Style

init()

FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]

BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]

BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]


def print_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    """Wrap en print() para color y brillo"""
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)