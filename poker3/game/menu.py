# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   扑克游戏的控制界面
# ------------------------(max to 80 columns)-----------------------------------

import os


def clear_menu():
    '清屏'
    i = os.system("cls")
    return


def prt_start():
    '打印游戏开始信息'
    clear_menu()
    print('***************************')
    print('* Poker Game Start        *')
    print('*       Made by 学员      *')
    print('*       Version 1.0       *')
    print('*       Updated 2019/7    *')
    print('***************************')
    return


def prt_end():
    '打印游戏结束信息'
    clear_menu()
    print('******************')
    print('**  GAME  OVER  **')
    print('******************')
    return


def prt_menu_a():
    '打印菜单a-选择玩法'
    clear_menu()
    print('**********************************')
    print('1 - 玩争上游（54张，不留底）')
    print('2 - 玩桥牌（4人52张，不带大小王）')
    print('3 - 玩 3 人斗地主（54张，留底3张）')
    print('4 - 玩 4 人斗地主（108张，留底8张）')
    print('其他数字 - 退出游戏')
    print('**********************************')
    print('请输入需要玩的游戏 (1-4)：', end='')
    return
