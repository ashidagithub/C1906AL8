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
    print('***************************')
    print('* Poker Game Start        *')
    print('*       Made by 学员英文名 *')
    print('***************************')
    return


def prt_menu_a():
    '打印菜单a-选择玩法'
    print('**********************************')
    print('1 - 玩争上游（54张，不留底）')
    print('2 - 玩3人斗地主（54张，留底3张）')
    print('3 - 玩4人斗地主（108张，留底8张）')
    print('4 - 玩桥牌（4人52张，不带大小王）')
    print('**********************************')
    print('请输入需要玩的游戏 (1-4)：', end='')
    return


def prt_menu_b(play_type):
    '打印菜单b-挑选自己的牌并按金字塔形显示'
    return

def prt_menu_c(my_deck):
    '打印菜单c-出牌'
    return
