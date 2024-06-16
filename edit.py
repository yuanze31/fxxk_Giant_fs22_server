import os
import subprocess
import time
import xml.etree.ElementTree as ET


def edit_gamename(gamename):
    gamename_status = "不修改服务器名称"
    WindowsUsername = os.getlogin()
    if gamename != "":
        config_path = f"C:/Users/{WindowsUsername}/Documents/My Games/FarmingSimulator2022/dedicated_server/dedicatedServerConfig.xml"
        tree = ET.parse(config_path)
        root = tree.getroot()
        for game_name in root.iter("game_name"):
            game_name.text = str(gamename)
        tree.write(config_path)
        gamename_status = "服务器名称：" + gamename + "\n"
    return gamename_status


def edit_gamepswd(gamepswd):
    gamepswd_status = "不修改服务器密码"
    WindowsUsername = os.getlogin()
    if gamepswd != "":
        config_path = f"C:/Users/{WindowsUsername}/Documents/My Games/FarmingSimulator2022/dedicated_server/dedicatedServerConfig.xml"
        tree = ET.parse(config_path)
        root = tree.getroot()
        for game_password in root.iter("game_password"):
            game_password.text = str(gamepswd)
        tree.write(config_path)
        gamepswd_status = "服务器密码：" + gamepswd + "\n"
    return gamepswd_status


def edit_gameport(gameport):
    gameport_status = "不修改服务器端口"
    WindowsUsername = os.getlogin()
    if gameport != "":
        config_path = f"C:/Users/{WindowsUsername}/Documents/My Games/FarmingSimulator2022/dedicated_server/dedicatedServerConfig.xml"
        tree = ET.parse(config_path)
        root = tree.getroot()
        for port in root.iter("port"):
            port.text = str(gameport)
        tree.write(config_path)
        gameport_status = "服务器名称：" + gameport + "\n"
    return gameport_status


def edit_gameslot(gameslot):
    gameslot_status = "不修改存档槽"
    WindowsUsername = os.getlogin()
    if gameslot != "":
        config_path = f"C:/Users/{WindowsUsername}/Documents/My Games/FarmingSimulator2022/dedicated_server/dedicatedServerConfig.xml"
        tree = ET.parse(config_path)
        root = tree.getroot()
        for savegame_index in root.iter("savegame_index"):
            savegame_index.text = str(gameslot)
        tree.write(config_path)
        gameslot_status = "存档槽：" + gameslot + "\n"
    return gameslot_status


def edit_maxplayer(maxplayer):
    maxplayer_status = "不修改最大人数"
    WindowsUsername = os.getlogin()
    if maxplayer != "":
        config_path = f"C:/Users/{WindowsUsername}/Documents/My Games/FarmingSimulator2022/dedicated_server/dedicatedServerConfig.xml"
        tree = ET.parse(config_path)
        root = tree.getroot()
        for max_player in root.iter("max_player"):
            max_player.text = str(maxplayer)
        tree.write(config_path)
        maxplayer_status = "最大人数：" + maxplayer + "\n"
    return maxplayer_status


def edit_autosaveinterval(autosaveinterval):
    autosaveinterval_status = "不修改自动保存间隔"
    WindowsUsername = os.getlogin()
    if autosaveinterval != "":
        config_path = f"C:/Users/{WindowsUsername}/Documents/My Games/FarmingSimulator2022/dedicated_server/dedicatedServerConfig.xml"
        tree = ET.parse(config_path)
        root = tree.getroot()
        for auto_save_interval in root.iter("auto_save_interval"):
            auto_save_interval.text = str(autosaveinterval)
        tree.write(config_path)
        autosaveinterval_status = "自动保存间隔：" + autosaveinterval + "\n"
    return autosaveinterval_status


def start_game():
    WindowsUsername = os.getlogin()
    print("即将在3秒后启动，使用 Ctrl + C 取消")
    time.sleep(3)
    print("启动中...")
    # Steam路径
    steam_path = "C:\\Program Files (x86)\\Steam\\Steam.exe"
    # 游戏ID
    game_id = "1248130"
    # 启动参数
    launch_options = (
        '-name FS22 -profile "C:/Users/'
        + WindowsUsername
        + '/Documents/My Games/FarmingSimulator2022" -server'
    )

    command = f'"{steam_path}" -applaunch {game_id} {launch_options}'
    subprocess.run(command)
