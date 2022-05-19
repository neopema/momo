from colorfull import input_momo, print_color, FORES, BACKS, BRIGHTNESS
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
        print_color(line, color=FORES[5], brightness=BRIGHTNESS[1])
        time.sleep(0.05)

    print("\n\n")
    print_color("created by", )
    time.sleep(0.2)
    # clear()

def default_command_line():
    return input_momo("momo~ > ", color=FORES[7], brightness=BRIGHTNESS[1])
