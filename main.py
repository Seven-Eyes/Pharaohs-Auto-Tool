import os
import subprocess
import sys
import time
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
        print_colored("{r}[{ww}•{r}] All packages are already installed!", Fore.GREEN, Style.BRIGHT)
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
                
            threading.Thread(target=run_css).start()
            print_colored(f"{r}[{ww}•{r}] {g}Successfully start collecting points {g}✓", Fore.RED, Style.BRIGHT)
            
        elif cmd == '3':
        	stop()
        	print_colored(f"{r}[{ww}•{r}] {g}Successfully stop collecting points {g}✓", Fore.RED, Style.BRIGHT)
        	
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
    db.set("collect", False)
    
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
    api_id = "22256614"
    api_hash = "4f9f53e287de541cf0ed81e12a68fa3b"
    sleep = db.get("sleep") if db.exists("sleep") else 3
    async with TelegramClient('session', api_id, api_hash) as client:
        channel_username = '@JJ3BOT'
        channel_entity = await client.get_entity(channel_username)
        
        while True:
            sleep = db.get("sleep") if db.exists("sleep") else 3
            await client.send_message(channel_username, '/start')
            sleep(sleep)
            message = await client.get_messages(channel_username, limit=1)
            
            if "يجب عليك الاشتراك بقناة البوت" in message[0].message:
                match = re.search(r'@(\w+)', message[0].message)
                await client(JoinChannelRequest(match.group(0)))
                continue
            else:
                break

        sleep(sleep)
        await message[0].click(2)
        sleep(sleep)
        next_message = await client.get_messages(channel_username, limit=1)
        await next_message[0].click(2)
        sleep(sleep)

        while True:
            if db.get("collect") == False:
                break
            sleep = db.get("sleep") if db.exists("sleep") else 3
            sleep(sleep)
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
    
if __name__ == "__main__":
    try:
        start_interface()
        main_page()
    except KeyboardInterrupt:
        exit_message()