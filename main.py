# -*- coding: UTF-8 -*-

# date: 2024-06-16
# author: yuanze31
# version: 1.1.0
#
# ——--————/´ ¯/)
# —— ———--/—-/
# — ————-/—-/
# ———--/´¯/'--'/´¯`•_
# ———-/'/--/—-/—--/¨¯\
# ——--('(———- ¯~/'--')
# — ——\————-'—--/ FUCK YOU GIANT
# ———-'\'————_-•´
# — ———\———--)
# —— ——-\———-\

import os
import xml.etree.ElementTree as ET

import edit

# 初始化


def menu():
    while True:
        os.system("cls")
        print("--------------")
        print("FUCK YOU GIANT")
        print("--------------")
        print("FS22 便捷服务器面板 V1.1.0\n")
        print("1 - 启动服务器")
        print("2 - 修改服务器名称")
        print("3 - 修改服务器端口")
        print("4 - 修改游戏密码")
        print("5 - 修改存档槽位")
        print("6 - 修改最大人数")
        print("7 - 修改自动保存间隔")
        print("99 - 退出")

        choice = input("请输入你的选择: ")
        if choice == "1":  # 启动服务器
            os.system("cls")
            edit.start_game()
            break
        elif choice == "2":  # 修改服务器名称
            os.system("cls")
            print("更改服务器名称（非中文），回车不修改\n请勿输入无关字符")
            gamename = input()
            print(edit.edit_gamename(gamename))
        elif choice == "3":  # 修改游戏端口
            os.system("cls")
            print("更改服务器端口（纯数字），回车不修改\n请勿输入无关字符")
            gameport = input()
            print(edit.edit_gameport(gameport))
        elif choice == "4":  # 修改游戏密码
            os.system("cls")
            print("更改服务器密码（非中文），回车不修改\n请勿输入无关字符")
            gamepswd = input()
            print(edit.edit_gamepswd(gamepswd))
        elif choice == "5":  # 修改存档槽位
            os.system("cls")
            print("更改使用的存档槽（纯数字），回车不修改\n请勿输入无关字符")
            gameslot = input()
            print(edit.edit_gameslot(gameslot))
        elif choice == "6":  # 修改最大人数
            os.system("cls")
            print("更改最大人数（纯数字），回车不修改\n请勿输入无关字符")
            maxplayer = input()
            print(edit.edit_maxplayer(maxplayer))
        elif choice == "7":  # 修改自动保存间隔
            os.system("cls")
            print("修改自动保存间隔（纯数字、秒），回车不修改\n请勿输入无关字符")
            auto_save_interval = input()
            print(edit.edit_autosaveinterval(auto_save_interval))
        elif choice == "99":  # 退出
            break
        else:
            os.system("cls")


if __name__ == "__main__":
    menu()
