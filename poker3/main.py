# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   模拟一个发牌机器和一个发牌员的场景
#   Ver 3.0
# ------------------------(max to 80 columns)-----------------------------------

import time
import os

# import our modules
from game.menu import *


# ----------
prt_start()
time.sleep(3)  # 延迟3秒

clear_menu()
prt_menu_a()
game_type = int(input())
