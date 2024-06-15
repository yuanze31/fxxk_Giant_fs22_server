# -*- coding: UTF-8 -*-

# date: 2024-06-16
# author: yuanze31
# version: 1.0.0
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
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

import keyboard

# 初始化
WindowsUsername = os.getlogin()
gamename_status = "服务器名称：不修改\n"
gameslot_status = "存档槽：不修改\n"


def edit_gamename():
    global gamename_status
    print("更改game_name，回车不修改直接启动\n请勿输入无关字符")
    gamename = input()
    if gamename != "":
        # 构建文件路径
        config_path = f"C:/Users/{WindowsUsername}/Documents/My Games/FarmingSimulator2022/dedicated_server/dedicatedServerConfig.xml"
        # 解析XML文件
        tree = ET.parse(config_path)
        root = tree.getroot()
        # 更新<game_name>
        for game_name in root.iter("game_name"):
            game_name.text = str(gamename)
        # 保存
        tree.write(config_path)
        gamename_status = "服务器名称：" + gamename + "\n"


def edit_gameslot():
    global gameslot_status
    print("更改gameslot，回车不修改直接启动\n请勿输入无关字符")
    gameslot = input()
    if gameslot != "":
        # 构建文件路径
        config_path = f"C:/Users/{WindowsUsername}/Documents/My Games/FarmingSimulator2022/dedicated_server/dedicatedServerConfig.xml"
        # 解析XML文件
        tree = ET.parse(config_path)
        root = tree.getroot()
        # 更新<savegame_index>
        for savegame_index in root.iter("savegame_index"):
            savegame_index.text = str(gameslot)
        # 保存
        tree.write(config_path)
        gameslot_status = "存档槽：" + gameslot + "\n"


def start_game():
    print("即将在3秒后启动，使用 Ctrl + C 取消")
    time.sleep(3)
    print("启动中...")
    # Steam路径
    steam_path = "C:\\Program Files (x86)\\Steam\\Steam.exe"
    # 游戏ID
    game_id = "1248130"
    # 启动参数
    launch_options = '-name FS22 -profile "C:/Users/15389/Documents/My Games\\FarmingSimulator2022" -server'

    command = f'"{steam_path}" -applaunch {game_id} {launch_options}'
    subprocess.run(command)


print("是否快速启动？\n回车-是   N-否")
fast_start = input()
if fast_start == "":
    start_game()
    sys.exit(0)
else:
    edit_gamename()
    edit_gameslot()

print("游戏即将启动，请验证以下参数\n" + gamename_status + gameslot_status)
print("输入Y确认启动")
will_start = input()
if will_start == "Y" or will_start == "y":
    start_game()
else:
    print("取消启动")
    print("按任意键退出...")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            break
