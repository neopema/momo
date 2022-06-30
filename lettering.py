from colorfull import input_momo, print_color, TITLES_FORES, FORES, BRIGHTNESS
from uftools import clear

import time


default_welcome_title = ["    :::       ::: :::::::::: :::        ::::::::   ::::::::    :::   :::   ::::::::::      ::::::::::: :::::::: " ,
"   :+:       :+: :+:        :+:       :+:    :+: :+:    :+:  :+:+: :+:+:  :+:                 :+:    :+:    :+: ",
"  +:+       +:+ +:+        +:+       +:+        +:+    +:+ +:+ +:+:+ +:+ +:+                 +:+    +:+    +:+  ",
" +#+  +:+  +#+ +#++:++#   +#+       +#+        +#+    +:+ +#+  +:+  +#+ +#++:++#            +#+    +#+    +:+   ",
"+#+ +#+#+ +#+ +#+        +#+       +#+        +#+    +#+ +#+       +#+ +#+                 +#+    +#+    +#+    ",
"#+#+# #+#+#  #+#        #+#       #+#    #+# #+#    #+# #+#       #+# #+#                 #+#    #+#    #+#     ",
"###   ###   ########## ########## ########   ########  ###       ### ##########          ###     ########       ",
"        :::   :::                   ::::::::                     :::   :::                   ::::::::           ",
"      :+:+: :+:+:                 :+:    :+:                   :+:+: :+:+:                 :+:    :+:           ",
"    +:+ +:+:+ +:+                +:+    +:+                  +:+ +:+:+ +:+                +:+    +:+            ",
"   +#+  +:+  +#+                +#+    +:+                  +#+  +:+  +#+                +#+    +:+             ",
"  +#+       +#+                +#+    +#+                  +#+       +#+                +#+    +#+              ",
" #+#       #+#                #+#    #+#                  #+#       #+#                #+#    #+#               ",
"###       ###                 ########                   ###       ###                 ########         v0.0.1"]

def default_welcome():

    for i, line in enumerate(default_welcome_title):
        print_color(line, color=TITLES_FORES[i], brightness=BRIGHTNESS[1])
        time.sleep(0.05)

    print("\n\n")
    time.sleep(0.2)
    # clear()


def default_command_line():
    return input_momo("momo~ >", color=FORES[7], brightness=BRIGHTNESS[1])


def first_welcome():
    print('Bienvenido a Momo.\n Antes de comenzar vamos a configurar algunas cosas :)')
    time.sleep(0.3)
    print('\n')


def first_hello(name):
    clear()
    print(f"Mucho gusto {name}, soy Momo y sere tu asistente virtual.")
    time.sleep(0.8)
    print("Espero por mucho tiempo, je je je")
    time.sleep(0.7)
    print('Estoy terminando de configurarme, dame un momento')
    time.sleep(0.8)
    print('...')
    time.sleep(0.5)
    print('...')
    time.sleep(0.7)
    print('...')