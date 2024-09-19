import os
import requests
import zipfile
import tempfile
import shutil
import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

folder_name = "Pharaohs-Auto-Tool"
repo_url = "https://github.com/Seven-Eyes/Pharaohs-Auto-Tool"
main_file = os.path.join(folder_name, "main.py")

if os.path.exists(folder_name):
    if os.path.exists(main_file):
        print(Fore.GREEN + "Running tool . . .")
        subprocess.run(["python", main_file])
    else:
        print(Fore.RED + "some files is missing.")
else:
    with tempfile.TemporaryDirectory() as temp_dir:
        zip_url = f"{repo_url}/archive/refs/heads/main.zip"
        zip_path = os.path.join(temp_dir, "latest_version.zip")

        print(Fore.YELLOW + "Downloading the repository...")
        response = requests.get(zip_url)
        if response.status_code == 200:
            with open(zip_path, "wb") as f:
                f.write(response.content)

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)

            extracted_folder = os.path.join(temp_dir, "Pharaohs-Auto-Tool-main")
            if os.path.exists(extracted_folder):
                shutil.move(extracted_folder, folder_name)
            else:
                print(Fore.RED + "Extracted folder is missing.")
    
    if os.path.exists(main_file):
        print(Fore.GREEN + "Running main.py...")
        subprocess.run(["python", main_file])
    else:
        print(Fore.RED + "main.py is missing after download.")