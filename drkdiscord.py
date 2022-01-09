#!/usr/bin/python3

#####################################################
## DarkDiscord (DrkDC)                             ##
## A useful tool to gen/check discord stuff        ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
#####################################################

# Imports
import time
import pyfade
import random
from colorama import Fore, Style, init
import os
import requests

# Global Variables
drk = 14


# Defines
def banner():
  print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_red, """
   V. 0.0.1 Alpha (January 9th 2022)
  ██████╗ ██████╗ ██╗  ██╗    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
  ██╔══██╗██╔══██╗██║ ██╔╝    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
  ██║  ██║██████╔╝█████╔╝     ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
  ██║  ██║██╔══██╗██╔═██╗     ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
  ██████╔╝██║  ██║██║  ██╗    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝                                  
                                                                          """))
  print(f'''{Fore.LIGHTWHITE_EX}                                [ Made by {Fore.YELLOW}drk#1337 {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  ''')

def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')
  
def underdev():
  print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} This section is currently under development.")
def back():
  input(f"{Fore.YELLOW}\nPress enter to go back.")
def options():
  clearcmd()
  banner()
  print("""
  [1] Token Generator 
  [2] Token Checker (Under Development)
  [3] Nitro Gift Generator
  [4] Nitro Gift Checker (Not Stable)
  [5] Coming Soon 

  [6] Credits
  [7] Settings
  [8] Quit
  
  """)
  USER_OPTION = input("Option: ")
  if USER_OPTION == "1":
    clearcmd()
    generatetoken()
  elif USER_OPTION == "2":
    underdev()
    back()
    options()
  elif USER_OPTION == "3":
    clearcmd()
    nitrogenerator()
  elif USER_OPTION == "4":
    clearcmd()
    nitrocheck()
  elif USER_OPTION == "5":
    underdev()
    back()
    options()
  elif USER_OPTION == "6":
    underdev()
    back()
    options()
  elif USER_OPTION == "7":
    underdev()
    back()
    options()
  elif USER_OPTION == "8":
    clearcmd()
    quit()
  else:
    print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Did not reckognize your input {Fore.YELLOW}{USER_OPTION}{Fore.LIGHTWHITE_EX}. Please enter one of the numbers above.")
    back()
    options()
    


def generatetoken():

  token_start = "OTI3MDM"
  random_letters = "abcdefghijklmnopqrstuwyxzABCDEFGHIJKLMNOPQRSTUWYXZ1234567890"
  random_letterswunder = "abcdefghijklmnopqrstuwyxzABCDEFGHIJKLMNOPQRSTUWYXZ_"
  random_letterswboth = "abcdefghijklmnopqrstuwyxzABCDEFGHIJKLMNOPQRSTUWYXZ_-"
  random_lettersf = "0z"


  drk = "king"
  length = 51
  print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_cyan, """
   DRK DISCORD
  ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗     ██████╗ ███████╗███╗   ██╗
  ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝ ██╔════╝████╗  ██║
     ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║  ███╗█████╗  ██╔██╗ ██║
     ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║   ██║██╔══╝  ██║╚██╗██║
     ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ╚██████╔╝███████╗██║ ╚████║
     ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                                           
                                                                          """))
  print(f"""{Fore.LIGHTWHITE_EX} [ Made by {Fore.YELLOW}drk#1337 {Fore.LIGHTWHITE_EX}]{Fore.GREEN} DRK DISCORD PROJECT
  {Fore.LIGHTWHITE_EX}
  """)
  print("[*] Setting Up...\n")
  time.sleep(1)

  howmany = input(f"{Fore.BLUE}[?] How many tokens do you want to generate: ")

  with open("./generated/token/tokens.txt", "w+") as file:
      for i in range(int(howmany)):
          firstrandom = ''.join(random.choice(random_letters) for i in range(15))
          secondrandom = ''.join(random.choice(random_letterswboth) for i in range(3))
          thirdrandom = ''.join(random.choice(random_letterswunder) for i in range(26))

          result = token_start + firstrandom + "." + "YdEV" + secondrandom + "." + thirdrandom 
          file.write(result)
          file.write("\n")

      print(f"\n{Fore.YELLOW}[*] Generating... \n")
      time.sleep(2)
      print(f"{Fore.GREEN}[+] Generated {Fore.RED} {howmany} {Fore.GREEN} Discord token(s). Saved to ./generated/token/tokens.txt ")
      file.close()
      back()
      options()
def nitrogenerator():

  randomgift = "https://discord.gift/N2td3PXwMdFCRgyj" # Just an expired link to watch.
  characters = "abcdefghijklmnopqrstuwyxzABCDEFGHIJKLMNOPQRSTUWYXZ1234567890"
  
  print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_cyan, """
   DRK DISCORD
  ███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗ ███████╗███╗   ██╗
  ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║
  ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║
  ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║
  ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║
  ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                                      
                                                                          """))
  print(f"""{Fore.LIGHTWHITE_EX} [ Made by {Fore.YELLOW}drk#1337 {Fore.LIGHTWHITE_EX}]{Fore.GREEN} DRK DISCORD PROJECT
  {Fore.LIGHTWHITE_EX}
  """)
  print("[*] Setting Up...\n")
  time.sleep(1)

  howmany = input(f"{Fore.BLUE}[?] How many tokens do you want to generate?: ")

  with open("./generated/nitro/nitro.txt", "w+") as file:
      for i in range(int(howmany)):
          genrandom = ''.join(random.choice(characters) for i in range(16))

          result = f"https://discord.gift/{genrandom}" 
          file.write(result)
          file.write("\n")
      print(f"\n{Fore.YELLOW}[*] Generating... \n")
      time.sleep(2)
      print(f"{Fore.GREEN}[+] Generated {Fore.RED}{howmany}{Fore.GREEN} Discord token(s). Saved to ./generated/nitro/nitro.txt ")

  back()
  file.close()
  options()

def nitrocheck():
  init()

  print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_cyan, """
   DRK DISCORD
  ███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
  ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
  ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║     ███████║█████╗  ██║     █████╔╝ 
  ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
  ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
  ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
                                                                                    
                                                                      
                                                                          """))
  print(f"""{Fore.LIGHTWHITE_EX} [ Made by {Fore.YELLOW}drk#1337 {Fore.LIGHTWHITE_EX}]{Fore.GREEN} DRK DISCORD PROJECT
  {Fore.LIGHTWHITE_EX}
  """)
  print("[*] Setting Up...\n")
  time.sleep(1)
  def checkNitro(code):
    
    URL = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(URL)
    if response.status_code == 200:
        return True
    else: 
        return False
 
  
  VALID_CODES_FILE   = "./generated/nitro/valid_nitro_codes.txt"
  INVALID_CODES_FILE = "./generated/nitro/invalid_nitro_codes.txt"
  CODES_FILE         = "./generated/nitro/nitro.txt"
  if not os.path.exists(CODES_FILE):
    print("No file with nitro was found, Go Generate some bro..")
    back()
    options()
  validTokens_file   = open(VALID_CODES_FILE, "w+")
  invalidTokens_file = open(INVALID_CODES_FILE, "w+")
  
  with open(CODES_FILE , "r+") as codes_file:
      content = codes_file.readlines()
      codes = list(filter(None, list(map(lambda x: str.replace(x, "\n", ""), content))))
  
      for code in codes:
          status = checkNitro(code)
          if status is True:
              print(f'{Fore.GREEN}Valid {Fore.LIGHTWHITE_EX}| {code}', Fore.WHITE + Style.NORMAL)
              validTokens_file.write(code + "\n")
          else:
              print(f'{Fore.RED}Invalid {Fore.LIGHTWHITE_EX}| {code}', Fore.WHITE + Style.NORMAL)
              invalidTokens_file.write(code + "\n")

      codes_file.flush()
      os.fsync(codes_file.fileno())
      codes_file.close()
  print(f"{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Script Done!")
  back()
  options()


# Main Define
def main():
  clearcmd()
  print(f"""
                          {Fore.RED}LICENSE AGREEMNT\n{Fore.LIGHTWHITE_EX}
                      GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it and removing credits is not allowed.

 {Fore.YELLOW}https://github.com/DaRkSurface/drkdiscord/blob/main/LICENSE
  """)
  time.sleep(3.3)
  options()
main()
