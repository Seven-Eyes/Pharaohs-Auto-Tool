import os
import subprocess
import sys
import time
import shutil
import zipfile
import importlib, asyncio, webbrowser, re, json, threading

try:
    from colorama import init, Fore, Style
except:
    os.system('pip install colorama')
    os.system('cls' if os.name == 'nt' else 'clear')
    from colorama import init, Fore, Style
from time import sleep
from plugins.ascii_art import list_ascii
if not os.path.isdir('dbs'):
    os.mkdir('dbs')

print("\n"+list_ascii[3]+"\n\n")
r = '\033[31m'
b = '\033[36m'
y = '\033[33m'
g = '\033[32m'
p = '\033[1;34m'
ww = '\033[37m'

init()

def print_colored(text, color, style=Style.NORMAL):
    print(f"{style}{color}{text}{Style.RESET_ALL}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(duration=3, message="Loading ..."):
    chars = ['|', '/', '-', '\\']
    print_colored(f"{r}[{ww}•{r}] {g}The tool is starting, please waiting ..", Fore.YELLOW, Style.BRIGHT)
    for _ in range(duration * 3):
        for char in chars:
            print(f'\r{message} {char}', end='', flush=True)
            time.sleep(0.2)
    print("\r", end="")

def check_update(duration=3, message="Loading ..."):
    chars = ['|', '/', '-', '\\']
    for _ in range(duration * 3):
        for char in chars:
            print(f'\r• {g}{message} {ww}{char}', end='', flush=True)
            time.sleep(0.2)
    print("\r", end="")
    
def install_package(package_name):
    print_colored(f"Installing {package_name} ...", Fore.CYAN, Style.BRIGHT)
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    print_colored(f"{package_name} installed successfully!", Fore.GREEN, Style.BRIGHT)
    time.sleep(1)
    clear_screen()

def check_package_installed(package_name):
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False

def main():
    packages = ["requests", "telethon", "kvsqlite", "colorama", "webbrowser"]
    not_installed = []

    loading_animation(duration=3, message="Verifying packages")

    for package in packages:
        if not check_package_installed(package):
            not_installed.append(package)

    if not_installed:
        print_colored(f"{r}[{ww}•{r}] Some packages are not installed:", Fore.RED, Style.BRIGHT)
        for package in not_installed:
            print_colored(f"- {package}", Fore.RED)
        for package in not_installed:
            install_package(package)
    else:
        print_colored(f"{r}[{ww}•{r}] {g}All packages are already installed!", Fore.GREEN, Style.BRIGHT)
        sleep(3)
main()

def start_interface():
    clear_screen()
    s_i = f"""{list_ascii[1]}
"""
    for i in s_i.splitlines():
        time.sleep(0.005)
        print(i)

def main_page():
    ma=f'''
{r}[ {ww}1{r} ] {b}Add & manage account.
{r}[ {ww}2{r} ] {b}Start collecting Pharaohs' coins.
{r}[ {ww}3{r} ] {b}Stop collecting Pharaohs' coins.
{r}[ {ww}4{r} ] {b}Set sleep collecting.
{r}[ {ww}5{r} ] {b}Check updates
{r}[ {ww}6{r} ] {b}Follow Us

'''
    for w in ma:
        sys.stdout.write(w)
        sys.stdout.flush()
        sleep(0.001)
        
    while True :
        cmd = input(f'''\033[1;34m[ {r}-{p} ] \033[31{os.getlogin()}@user\033[37m:\033[36m~\033[37m# ''')
        if cmd == '1':
            clear_screen()
            manage_account()
            
        elif cmd == 'help':
            help()
            
        elif cmd == 'exit':
            print_colored(f"{r}[{ww}•{r}] {g}You have exited the tool. Goodbye!", Fore.RED, Style.BRIGHT)
            exit()
            
        elif cmd == 'clear' or cmd == 'cls':
            clear_screen()
            
        elif cmd == '2':
            if not os.path.exists("session.session"):
                print('\033[31m[×] \033[37mThere are no registered accounts\033[37m')
                continue
            threading.Thread(target=run_css).start()
            print_colored(f"{r}[{ww}•{r}] {g}Successfully start collecting points {g}✓", Fore.RED, Style.BRIGHT)
            
        elif cmd == '3':
        	x = stop()
        	if x:
        	    print_colored(f"{r}[{ww}•{r}] {g}Successfully stop collecting points {g}✓", Fore.RED, Style.BRIGHT)
        	else:
        	    print_colored(f"{r}[{ww}•{r}] Collecting is already stopped {r}x", Fore.RED, Style.BRIGHT)
        	
        elif cmd == '4':
        	set_sleep()
        	
        elif cmd == '5':
        	check_updates()
        	
        elif cmd == '6':
        	clear_screen()
        	follow_us()
        	
        elif cmd == "":
            continue
            
        else:
        	print('\033[31m[×] \033[37mYou must enter a valid choice')

def exit_message():
    print_colored(f"{r}[{ww}•{r}] {g}You have exited the tool. Goodbye!", Fore.RED, Style.BRIGHT)

def follow_us():
	s_i = f"""{list_ascii[4]}
"""
	for i in s_i.splitlines():
	    time.sleep(0.005)
	    print(i)
	ma=f'''
{r}[ {ww}1{r} ] {b}Telegram channel.
{r}[ {ww}2{r} ] {b}Contact the developer.
{r}[ {ww}3{r} ] {b}Pharaohs bot.
{r}[ {ww}0{r} ] {b}Back.

'''
	for w in ma:
	    sys.stdout.write(w)
	    sys.stdout.flush()
	    sleep(0.001)
	while True :
	    cmd = input(f'''\033[1;34m[ {r}-{p} ] \033[31{os.getlogin()}@user\033[37m:\033[36m~\033[37m# ''')
	    if cmd == "0":
	        start_interface()
	        main_page()
	    elif cmd == "1":
	        webbrowser.open('https://t.me/Se7en_Eyes')
	        
	    elif cmd == "2":
	        webbrowser.open('https://t.me/RReRe')
	        
	    elif cmd == "3":
	        webbrowser.open('https://t.me/JJ3BOT')
	        
	    elif cmd == "":
	        continue
	    else:
	        print('\033[31m[×] \033[37mYou must enter a valid choice')

from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon import TelegramClient, sync
from telethon import events
from telethon.tl.custom import Button
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
from bs4 import BeautifulSoup
import time
import re, threading
from time import sleep
try:
    from telethon.sessions import StringSession
    from kvsqlite.sync import Client as uu
    from telethon import TelegramClient, events, functions, types
    from telethon.errors import (
        ApiIdInvalidError,
        PhoneNumberInvalidError,
        PhoneCodeInvalidError,
        PhoneCodeExpiredError,
        SessionPasswordNeededError,
        PasswordHashInvalidError
    )
except:
    os.system("pip install telethon kvsqlite")
    try:
        from telethon.sessions import StringSession
        from kvsqlite.sync import Client as uu
        from telethon import TelegramClient, events, functions, types
        from telethon.errors import (
            ApiIdInvalidError,
            PhoneNumberInvalidError,
            PhoneCodeInvalidError,
            PhoneCodeExpiredError,
            SessionPasswordNeededError,
            PasswordHashInvalidError
        )
    except Exception as errors:
        print('An Erorr with: ' + str(errors))
        exit(0)
db = uu('dbs/elhakem.ss', 'rshq')

def stop():
    if db.get("collect") == True or None:
        db.set("collect", False)
        return True
    else:
        return False
def set_sleep():
    while True:
        cmd = input(f'''{r}[{ww}•{r}] {b}Enter the number of sleeps in seconds: \033[37m''')
        try:
            sleep=int(cmd)
            db.set("sleep", sleep)
            print(f'{r}[{g}✓{r}] \033[37mSleep was set successfully.')
            break 
        except: print('\033[31m[×] \033[37mSleep must be in seconds only ')
        
def manage_account():
    clear_screen()
    s_i = f"""{list_ascii[0]}
"""
    for i in s_i.splitlines():
        time.sleep(0.005)
        print(i)
    ma=f'''
{r}[ {ww}1{r} ] {b}Add account.
{r}[ {ww}2{r} ] {b}Delete Account.
{r}[ {ww}0{r} ] {b}Back.

'''
    for w in ma:
	    sys.stdout.write(w)
	    sys.stdout.flush()
	    sleep(0.001)
    while True :
	    cmd = input(f'''\033[1;34m[ {r}-{p} ] \033[31{os.getlogin()}@user\033[37m:\033[36m~\033[37m# ''')
	    if cmd == "0":
	        start_interface()
	        main_page()
	        
	    elif cmd == "1":
	        add_account()
	        
	    elif cmd == "2":
	        cd = input(f'''\033[1;34m[ {r}-{p} ] {b}Do you want to delete the account? {ww}y/N\n\033[37m''')
	        if cd == "y" or cd == "Y":
	            if os.path.exists("session.session"):
	                os.remove("session.session")
	                if os.path.exists("session.session-journal"):
	                	os.remove("session.session-journal")
	                print(f'{r}[{g}✓{r}] \033[37mThe account has been successfully deleted.')
	            else:
	                print('\033[31m[×] \033[37mThere are no registered accounts\033[37m')
	                
	        elif cd == "n" or cd == "N":
	            manage_account()
	            
	    elif cmd == "":
	        continue
	    else:
	        print('\033[31m[×] \033[37mYou must enter a valid choice')
	            
def add_account():
    api_id, api_hash= None, None
    if os.path.exists("session.session"):
        return print('\033[31m[×] \033[37mYou must delete the account before registering a new account')
    while True:
        cmd = input(f'''{r}[{ww}•{r}] {b}Enter API_ID: \033[37m''')
        if cmd == "0":
	        start_interface()
	        main_page()
	        break
        try:
            api_id=int(cmd); 
            break 
        except: print('\033[31m[×] \033[37mAPI_ID must be in integers only ')
    while True:
        cmd = input(f'''{r}[{ww}•{r}] {b}Enter API_HASH: \033[37m''')
        if cmd == "0":
	        start_interface()
	        main_page()
	        break
        api_hash=cmd
        break
    try:
        with TelegramClient('session', api_id, api_hash) as client:
            client.start()
            print(f'{r}[{g}✓{r}] \033[37mThe account has been registered successfully.')
    except Exception as errors:
        print(f'An Erorr with: {r}' + str(errors))

def run_css():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(css())
    loop.run_forever() 
    
async def css():
    db.set("collect", True)
    api_id = "22256614"
    api_hash = "4f9f53e287de541cf0ed81e12a68fa3b"
    slp = db.get("sleep") if db.exists("sleep") else 3
    async with TelegramClient('session', api_id, api_hash) as client:
        channel_username = '@JJ3BOT'
        channel_entity = await client.get_entity(channel_username)
        
        while True:
            slp = db.get("sleep") if db.exists("sleep") else 3
            await client.send_message(channel_username, '/start')
            sleep(slp)
            message = await client.get_messages(channel_username, limit=1)
            
            if "يجب عليك الاشتراك بقناة البوت" in message[0].message:
                match = re.search(r'@(\w+)', message[0].message)
                await client(JoinChannelRequest(match.group(0)))
                continue
            else:
                break

        sleep(slp)
        await message[0].click(2)
        sleep(slp)
        next_message = await client.get_messages(channel_username, limit=1)
        await next_message[0].click(2)
        sleep(slp)

        while True:
            if db.get("collect") == False:
                break
            slp = db.get("sleep") if db.exists("sleep") else 3
            sleep(slp)
            history = await client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0,hash=0
            ))
            latest_message = history.messages[0]
            if 'لا يوجد قنوات في الوقت الحالي' in latest_message.message:
                print(f'{r}[{g}✓{r}] \033[37mThe channels are ended and the collecting is complete .')
                break
            try:
                url = latest_message.reply_markup.rows[0].buttons[0].url
                try:
                    await client(JoinChannelRequest(url))
                except:
                    invite_hash = url.split('/')[-1].replace("+", "")
                    await client(ImportChatInviteRequest(invite_hash))

                verify_message = await client.get_messages(channel_username, limit=1)
                await verify_message[0].click(text='تحقق')
            except Exception as e:
                print(f'An Erorr with: {r}' + str(e))
                print(f'{b}[{r}×{b}] {r}You have been blocked by Telegram from joining channels, come back later.')
                break

def check_updates():
    check_update(3, "Checking for updates, please wait ...")
    current = get_current_version()
    new = get_version_from_changelog()
    shutil.rmtree("temp_update")
    if current == new:
        print(f'{r}[{g}✓{r}] \033[37mYou are already using the latest version of the tool.')
    else:
        print(f'{r}[{g}!!{r}] {ww}New version found {g}{new} from the tool ')
        while True:
            cmd = input(f'{b}[{r}?{b}] {ww}Do you want to update the tool to the latest version? y/N\n')
            if cmd == "y" or cmd == "Y":
                check_update(4, "The update is installing, please wait ...")
                sta()
                print(f'{b}[{r}×{b}] {r}The update has been completed, please restart the tool.')
                exit()
            elif cmd == "n" or cmd == "N":
                print(f'{b}[{r}×{b}] {r}The update has been cancelled. ')
                break
            elif cmd == "":
                continue
                
def download_latest_version(repo_url, temp_dir="temp_update"):
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    zip_url = f"{repo_url}/archive/refs/heads/main.zip"
    zip_path = os.path.join(temp_dir, "latest_version.zip")

    response = requests.get(zip_url)
    if response.status_code == 200:
        with open(zip_path, "wb") as f:
            f.write(response.content)
    else:
        return False

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

    return temp_dir

def update_files(new_version_dir, excluded_files=["dbs", "session.session"]):
    for root, dirs, files in os.walk(new_version_dir):
        rel_path = os.path.relpath(root, new_version_dir)
        target_dir = os.path.join(os.getcwd(), rel_path)
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        for file in files:
            if file not in excluded_files:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(target_dir, file)
                shutil.copy(src_file, dest_file)

        dirs[:] = [d for d in dirs if d not in excluded_files]

def restart_tool():
    print("Restarting the tool...")
    os.execv(sys.executable, ['python'] + sys.argv)

def sta():
    repo_url = "https://github.com/Seven-Eyes/Pharaohs-Auto-Tool"
    new_version_dir = download_latest_version(repo_url)
    if not new_version_dir:
        return
    update_files(os.path.join(new_version_dir, "Pharaohs-Auto-Tool-main"))
    shutil.rmtree(new_version_dir)
    
def get_current_version():
    return "1.0.0"
    
def get_version_from_changelog():
    repo_url = "https://github.com/Seven-Eyes/Pharaohs-Auto-Tool"
    new_version_dir = download_latest_version(repo_url)
    if not new_version_dir:
        return
    changelog_path = os.path.join(os.path.join(new_version_dir, "Pharaohs-Auto-Tool-main"), "CHANGELOG.md")
    if os.path.exists(changelog_path):
        with open(changelog_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("## [") and "] - " in line:
                    match = re.search(r"## (.*?) -", line.replace("[", "").replace("]", ""))
                    version = match.group(1)
                    return version 
    return None
    
if __name__ == "__main__":
    try:
        start_interface()
        main_page()
    except KeyboardInterrupt:
        exit_message()