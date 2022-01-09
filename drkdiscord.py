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
from colorama import Fore
import os

# Global Variables
drk = 14


# Defines

def banner():
  print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_red, """
  V. 1.0 Beta (January 9th 2022)
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
  [4] Nitro Gift Checker (Under Development)
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
    underdev()
    back()
    options()
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
  print(f"""{Fore.LIGHTWHITE_EX} [ Made by {Fore.YELLOW}drk#1337 {Fore.LIGHTWHITE_EX}] WITH: {Fore.GREEN} DRK DISCORD PROJECT
  {Fore.LIGHTWHITE_EX}
  """)
  print("[*] Setting Up...\n")
  time.sleep(1.5)

  howmany = input(f"{Fore.BLUE}[?] How many tokens do you want to generate: ")

  with open("./generated/token/tokens.txt", "w+") as file:
      for i in range(int(howmany)):
          firstrandom = ''.join(random.choice(random_letters) for i in range(15))
          secondrandom = ''.join(random.choice(random_letterswboth) for i in range(3))
          thirdrandom = ''.join(random.choice(random_letterswunder) for i in range(26))

          result = token_start + firstrandom + "." + "YdEV" + secondrandom + "." + thirdrandom 
          file.write(result)
          file.write("\n")

      file.close()
      print(f"\n{Fore.YELLOW}[*] Generating... \n")
      time.sleep(2)
      print(f"{Fore.GREEN}[+] Generated {Fore.RED} {howmany} {Fore.GREEN} Discord token(s). Saved to ./generated/token/tokens.txt ")
      back()
      options()
def nitrogenerator():

  randomgift = "https://discord.gift/N2td3PXwMdFCRgyj" # Just an expired link to watch.
  characters = "abcdefghijklmnopqrstuwyxzABCDEFGHIJKLMNOPQRSTUWYXZ1234567890"
  length = 16
  drk = "king"
  
  print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_cyan, """
   DRK DISCORD
  ███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗ ███████╗███╗   ██╗
  ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║
  ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║
  ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║
  ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║
  ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                                      
                                                                          """))
  print(f"""{Fore.LIGHTWHITE_EX} [ Made by {Fore.YELLOW}drk#1337 {Fore.LIGHTWHITE_EX}] WITH: {Fore.GREEN} DRK DISCORD PROJECT
  {Fore.LIGHTWHITE_EX}
  """)
  print("[*] Setting Up...\n")
  time.sleep(1.5)

  howmany = input(f"{Fore.YELLOW}[?]{Fore.LIGHTWHITE_EX} How many tokens do you want to generate?: ")

  with open("./generated/nitro/nitro.txt", "w+") as file:
      for i in range(int(howmany)):
          genrandom = ''.join(random.choice(characters) for i in range(length))

          result = f"https://discord.gift/{genrandom}" 
          file.write(result)
          file.write("\n")
      print(f"\n{Fore.YELLOW}[*] Generating... \n")
      time.sleep(2)
      print(f"{Fore.GREEN}[+] Generated {Fore.RED} {howmany} {Fore.GREEN} Discord token(s). Saved to ./generated/nitro/nitro.txt ")

      file.close()
  back()
  options()


# Main Define
def main():
    options()
main()