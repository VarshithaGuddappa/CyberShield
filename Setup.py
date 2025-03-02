
try:
    import sys
    import os

    def OpenTelegram():
        try:
            import webbrowser
            from Program.Config.Config import telegram
            webbrowser.open(f'https://{telegram}')
        except: pass

    if sys.platform.startswith("win"):
        os.system("cls")
        print("Installing the python modules required for the RedTiger Tool:\n")
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")
        # OpenTelegram()
        os.system("python Tiger.py")

    elif sys.platform.startswith("linux"):
        os.system("clear")
        print("Installing the python modules required for the RedTiger Tool:\n")
        os.system("python3 -m pip3 install --upgrade pip")
        os.system("python3 -m pip3 install -r requirements.txt")
        # OpenTelegram()
        os.system("python3 Tiger.py")

except Exception as e:
    input(e)

