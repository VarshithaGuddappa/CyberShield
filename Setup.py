import sys
import os

def OpenTelegram():
    try:
        import webbrowser
        from Program.Config.Config import telegram
        webbrowser.open(f'https://{telegram}')
    except Exception as e:
        print(f"Error opening Telegram: {e}")

def run_authentication():
    try:
        os.system("cls" if sys.platform.startswith("win") else "clear")
        os.system("python autentication.py")  # Run the authentication script
    except Exception as e:
        print(f"Error during authentication: {e}")
        input("Press any key to exit.")

try:
    # Installation process
    if sys.platform.startswith("win"):
        os.system("cls")  # Clear screen for Windows
        print("Installing the Python modules required for the RedTiger Tool:\n")
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")  # Install dependencies
        run_authentication()  # Run the authentication after installing
        os.system("python Tiger.py")  # Run the main program

    elif sys.platform.startswith("linux"):
        os.system("clear")  # Clear screen for Linux
        print("Installing the Python modules required for the RedTiger Tool:\n")
        os.system("python3 -m pip3 install --upgrade pip")
        os.system("python3 -m pip3 install -r requirements.txt")  # Install dependencies
        run_authentication()  # Run the authentication after installing
        os.system("python3 Tiger.py")  # Run the main program

except Exception as e:
    input(f"An error occurred: {e}")
