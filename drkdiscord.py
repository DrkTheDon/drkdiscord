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
import discord
from datetime import datetime
from discord.ext import commands
import subprocess
import json
import asyncio
import sys


# Global Variables
drk = 14


# Defines
def error_msg():
  print(f"{Fore.RED}Error Bro.")
  input(f"{Fore.YELLOW}\nPress enter to quit.")
  clearcmd()
  quit()

def massdm():
  bot = discord.Client()

  def mdmbanner():
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
  
  with open("./selfbot/tokens.json", "r") as file:
    tokens = json.load(file)
  with open("./selfbot/usedtokens.json", "r") as file:
    checktokens = json.load(file)
  unusedtokens = []

  if len(tokens) == 0:
    print(f"No tokens were found in ./selfbot/tokens.json.\n {Fore.RED}Qutting..")
    time.sleep(1.5)
    quit()

  if len(unusedtokens) > 0:
    token = random.choice(unusedtokens)
    checktokens.append(token)
    with open("./selfbot/usedtokens.json", "w", enoding='utf-8') as file:
      json.dump(checktokens, file)
  else:
    reset = []
    with open("./selfbot/usedtokens.json", "w", encoding='utf-8') as file:
      json.dump(reset, file, ensure_ascii=False)
    print(f"{Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Resetting Tokens in ./selfbot/usedtokens.json")
    time.sleep(2.5)
  with open("./selfbot/config.json", "w+", enoding='utf-8') as file:
    config = json.load(file)
  min_cooldown = config['min_cooldown']
  max_cooldown = config['max_cooldown']
  display_sleep = config['display_sleep']
  message = config['message']
  dm_limit = config['dm_each_token']
  always_sleep = config['sleep_on_exception']
  duplicate = config['dm_already_dmed_users']
  fetch_users = config['always_fetch_users']
  send_embed = config['send_embed']
  embed_title = config['embed_title']
  embed_description = config['embed_description']
  embed_author = config['embed_author']
  embed_footer = config['embed_footer']
  embed_footer_icon_url = config['embed_footer_icon_url']
  embed_thumbnail_url = config['embed_thumbnail_url']
  embed_image_url = config['embed_image_url']
  embed_author_icon_url = config['embed_author_icon_url']
  if duplicate == "True":
    dpcl = "False"
  elif duplicate == "False":
    dpcl = "True"
  else:
    epcl = "False"
  
  async def massdm():
    with open("./selfbot/id.json", "r", encoding="utf-8") as file:
      ids = json.load(file)
    with open("./selfbot/blacklistedid.json", "r", encoding="utf-8") as file:
      blacklisted = json.load(file)
    index = 0
    success = 0
    for i in ids:
      with open("./selfbot/usedtokens.json", "r", encoding='utf-8') as file:
        usedtk = json.load(file)
      timenow = datetime.now()
      curtime = timenow.strftime("%Y-%m-%d")
      index += 1
      if int(i) in blacklisted:
        if fetch_users == "False":
          print(f"{Fore.RED}{curtime} {Fore.BLACK}[-] Blacklisted USERID {Fore.YELLOW}{i} {Fore.BLACK}{index} / {len(ids)}")
        elif fetch_users == "True":
          fetchusr = await bot.fetch_user(i)
          print(f"{Fore.RED}{curtime} {Fore.BLACK}[-] Blacklisted USERID {Fore.YELLOW}{fetchusr} {Fore.BLACK}{index} / {len(ids)}")
          print(f"{Fore.Blue} Wait...")
          await asyncio.sleep(2.5)
        else:
          print(f"{Fore.RED}ERROR WHILE FETCHING USER.")
          error_msg()
      elif dpcl == "False":
        if int(i) in usedtk:
          if fetch_users == "False":
            print(f"{Fore.RED}{curtime} {Fore.MAGENTA}[-] Avoiding Duplicated USERID {Fore.YELLOW}{i} {Fore.BLACK}{index} / {len(ids)}")
            print(f"{Fore.RED}{curtime} {Fore.MAGENTA}[-] Avoiding Duplicated USERID {Fore.YELLOW}{fetchusr} {Fore.BLACK}{index} / {len(ids)}")
            print(f"{Fore.Blue} Wait...")
            await asyncio.sleep(2.5)
          else:
            print(f"{Fore.RED}ERROR WHILE FETCHING USER.")
            error_msg()
        else:
          fetchusr = await bot.fetch_user(i)
          try:
            await fetchusr.send(message.replace('user_id', f'{fetchusr.id}').replace('user_name', f'{fetchusr.name}').replace('user_mention', f'<@{fetchusr.id}>').replace('user_discriminator', f'{fetchusr.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'))
            print(f"{Fore.RED}{curtime} {Fore.GREEN}[+] Sent {message} to {Fore.YELLOW}{fetchusr}{Fore.GREEN} {index} / {len(ids)}")
            cnm = random.randint(min_cooldown, max_cooldown)
            success += 1
            if success >= dm_limit:
              print(f"{Fore.RED}{curtime} {Fore.MAGENTA}[*] THE DM LIMIT HAS BEEN REACHED: {Fore.YELLOW}{dm_limit} Direct Messages {Fore.MAGENTA} Switching to other token.")
              await asyncio.sleep(1.5)
            if display_sleep == "True":
              print(f"{Fore.YELLOW}[*] Sleeping {cnm} seconds.")
            else:
              pass
            await asyncio.sleep(cnm)
          except discord.Forbidden as ex:
            if ex.code == 40003:
              print(f"{Fore.RED}[-] You have been ratelimited\n {Fore.YELLOW}[*] The code will continue in 90 seconds. - {Fore.RED} {ex}")
              await asyncio.sleep(90)
            else:
              print(f"{Fore.RED}{curtime}[-] Could not send a message to {Fore.YELLOW}{fetchusr}{Fore.RED} - {ex} {index} / {len(ids)}")
              cnm = random.randint(min_cooldown, max_cooldown)
              if always_sleep == "True":
                if display_sleep == "True":
                  print(f"{Fore.YELLOW}[*] Sleeping {cnm} seconds.")
                await asyncio.sleep(cnm)
          except discord.HTTPException as ex:
              print(f"{Fore.BLUE}{curtime} {Fore.RED}[-] Could not get {Fore.YELLOW}{i}{Fore.RED} - {ex} {index} / {len(ids)}")
          if fetchusr.id not in usedtk:
              await asyncio.sleep(0.01)
              usedtk.append(fetchusr.id)
              with open("./selfbot/usedtokens.json", "w+") as file:
                  await asyncio.sleep(0.01)
                  json.dump(usedtk, file)
      else:
        input(f"{Fore.GREEN}[+] Script DONE!")
        print("GITHUB: ")
        await sys.exit()

  async def massdmembed():
      with open("ids.json", "r", encoding='utf-8') as file:
          ids = json.load(file)
      with open("blacklistedids.json", "r", encoding='utf-8') as file:
          blacklisted = json.load(file)
      index = 0
      success = 0
      for i in ids:
          with open("alreadyusedids.json", "r", encoding='utf-8') as file:
              usedtks = json.load(file)
          now = datetime.now()
          curtime = now.strftime("%Y-%m-%d")
          index += 1
          if int(i) in blacklisted:
              if fetch_users == "False":
                  print(f"{Fore.BLUE}{curtime} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{i} {Fore.BLACK}{index} / {len(ids)}")
              elif fetch_users == "True":
                  fetchusr = await bot.fetch_user(i)
                  print(f"{Fore.BLUE}{curtime} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{fetchusr} {Fore.BLACK}{index} / {len(ids)}")
                  print(f"{Fore.YELLOW}Sleeping 2 seconds")
                  await asyncio.sleep(2)
              else:
                  print(f"{Fore.RED}[FETCH USERS ERROR]")
                  error_msg()
          elif fetchusr == "False":
              if int(i) in usedtks:
                  if fetch_users == "False":
                      print(f"{Fore.BLUE}{curtime} {Fore.LIGHTMAGENTA_EX}[x] Avoiding Duplicates: {Fore.YELLOW}{i} {Fore.BLACK}{index} / {len(ids)}")
                  elif fetch_users == "True":
                      fetchusr = await bot.fetch_user(i)
                      print(f"{Fore.BLUE}{curtime} {Fore.LIGHTMAGENTA_EX}[x] Avoiding Duplicates: {Fore.YELLOW}{fetchusr} {Fore.BLACK}{index} / {len(ids)}")
                      print(f"{Fore.YELLOW}Sleeping 2 seconds")
                      await asyncio.sleep(2)
                  else:
                      print(f"{Fore.RED}[FETCH USERS ERROR]")
                      error_msg()
              else:
                  fetchusr = await bot.fetch_user(i)
                  embed_skrr = discord.Embed(title=f"{embed_title}".replace('user_id', f'{fetchusr.id}').replace('user_name', f'{fetchusr.name}').replace('user_discriminator', f'{fetchusr.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'),icon_url=embed_footer_icon_url.replace('user_avatar', f'{fetchusr.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}'),description=f"{embed_description}".replace('user_id', f'{fetchusr.id}').replace('user_name',f'{fetchusr.name}').replace('user_mention', f'<@{fetchusr.id}>').replace('user_discriminator',f'{fetchusr.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'), color=discord.Colour.random())
                  embed_skrr.set_thumbnail(url=f"{embed_thumbnail_url}"), embed_skrr.set_image(url=f"{embed_image_url}"), embed_skrr.set_author(name=f"{embed_author}".replace('user_id', f'{fetchusr.id}').replace('user_name',f'{fetchusr.name}').replace('user_mention', f'<@{fetchusr.id}>').replace('user_discriminator',f'{fetchusr.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'), icon_url=embed_author_icon_url.replace('user_avatar',f'{fetchusr.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}')), embed_skrr.set_footer(text=f"{embed_footer}".replace('user_id', f'{fetchusr.id}').replace('user_name',f'{fetchusr.name}').replace('user_mention', f'<@{fetchusr.id}>').replace('user_discriminator',f'{fetchusr.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'),icon_url=embed_footer_icon_url.replace('user_avatar',f'{fetchusr.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}'))
                  try:
                      await fetchusr.send(embed=embed_skrr)
                      print(f"{Fore.BLUE}{curtime} {Fore.LIGHTGREEN_EX}[+] Sent the embed to {Fore.YELLOW}{fetchusr}{Fore.LIGHTGREEN_EX} {index} / {len(ids)}")
                      cnm = random.randint(min_cooldown, max_cooldown)
                      success += 1
                      if success >= dm_limit:
                          print(f"{Fore.BLUE}{curtime} {Fore.LIGHTCYAN_EX}[*] DM Limit has been reached: {Fore.YELLOW}{dm_limit} DMs {Fore.LIGHTCYAN_EX}(Switching the token in 1 second)")
                          await asyncio.sleep(1)
                          os.execv(sys.executable, ['python'] + sys.argv)
                      if display_sleep == "True":
                            print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                      else:
                          pass
                      await asyncio.sleep(pablo)
                  except discord.Forbidden as ex:
                      if ex.code == 40003:
                          print(f"{Fore.RED}[-] You have been ratelimited\n {Fore.YELLOW}[*] The code will continue in 90 seconds. - {Fore.RED} {ex}")
                          await asyncio.sleep(90)
                          continue
                      else:
                          print(
                              f"{Fore.BLUE}{curtime} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{fetchusr}{Fore.RED} - {ex} {index} / {len(ids)}")
                          cnm = random.randint(min_cooldown, max_cooldown)
                          if always_sleep == "True":
                              if display_sleep == "True":
                                  print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                              await asyncio.sleep(pablo)
                  except discord.HTTPException as ex:
                      print(f"{Fore.BLUE}{curtime} {Fore.RED}[-] Couldn\'t fetch {Fore.YELLOW}{i}{Fore.RED} - {ex} {index} / {len(ids)}")
                  if fetchusr.id not in usedtks:
                      usedtks.append(fetchusr.id)
                      with open("./selfbot/usedtokens.json", "w") as file:
                          json.dump(usedtks, file)
          else:
              try:
                  fetchusr = await bot.fetch_user(i)
                  embed_skrr = discord.Embed(title=f"{embed_title}".replace('user_id', f'{fetchusr.id}').replace('user_name',f'{fetchusr.name}').replace('user_discriminator', f'{fetchusr.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'),icon_url=embed_footer_icon_url.replace('user_avatar',f'{fetchusr.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}'), description=f"{embed_description}".replace('user_id', f'{fetchusr.id}').replace('user_name',f'{fetchusr.name}').replace('user_mention', f'<@{fetchusr.id}>').replace('user_discriminator', f'{fetchusr.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'), color=discord.Colour.random())
                  embed_skrr.set_thumbnail(url=f"{embed_thumbnail_url}"), embed_skrr.set_image(url=f"{embed_image_url}"), embed_skrr.set_author(name=f"{embed_author}".replace('user_id', f'{fetchusr.id}').replace('user_name',f'{fetchusr.name}').replace('user_mention', f'<@{fetchusr.id}>').replace('user_discriminator',f'{fetchusr.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'), icon_url=embed_author_icon_url.replace('user_avatar',f'{fetchusr.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}')), embed_skrr.set_footer(text=f"{embed_footer}".replace('user_id', f'{fetchusr.id}').replace('user_name',f'{fetchusr.name}').replace('user_mention', f'<@{fetchusr.id}>').replace('user_discriminator',f'{fetchusr.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'),icon_url=embed_footer_icon_url.replace('user_avatar',f'{fetchusr.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}'))
                  await fetchusr.send(embed=embed_skrr)
                  print(f"{Fore.BLUE}{curtime} {Fore.LIGHTGREEN_EX}[+] Sent the embed to {Fore.YELLOW}{fetchusr}{Fore.LIGHTGREEN_EX} {index} / {len(ids)}")
                  success +=1
                  if success >= dm_limit:
                      print(f"{Fore.BLUE}{curtime} {Fore.LIGHTCYAN_EX}[?] DM Limit has been reached: {Fore.YELLOW}{dm_limit} DMs {Fore.LIGHTCYAN_EX}(Switching the token in 1 second)")
                      await asyncio.sleep(1)
                  cnm = random.randint(min_cooldown, max_cooldown)
                  if display_sleep == "True":
                      print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                  else:
                      pass
                  await asyncio.sleep(cnm)
              except discord.Forbidden as ex:
                  if e.code == 40003:
                      print(f"{Fore.RED}[-] You have been ratelimited\n {Fore.YELLOW}[*] The code will continue in 90 seconds. - {Fore.RED} {ex}")
                      await asyncio.sleep(90)
                      os.execv(sys.executable, ['python'] + sys.argv)
                      continue
                  else:
                      print(f"{Fore.BLUE}{curtime} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{curtime}{Fore.RED} - {e} {index} / {len(ids)}")
                      pablo = random.randint(min_cooldown, max_cooldown)
                      if always_sleep == "True":
                          if display_sleep == "True":
                              print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                          await asyncio.sleep(pablo)
              except discord.HTTPException as e:
                  print(f"{Fore.BLUE}{curtime} {Fore.RED}[-] Couldn\'t fetch {Fore.YELLOW}{i}{Fore.RED} - {e} {index} / {len(ids)}")
              if fetchusr.id not in usedtks:
                  usedtks.append(fetchusr.id)
                  with open("alreadyusedids.json", "w") as file:
                      json.dump(usedtks, file)
      input(f"{Fore.GREEN}[+] Script DONE!")
      print("GITHUB: ")
      await sys.exit()

  mdmbanner()

  @bot.event
  async def on_ready():
      if send_embed == "False":
          await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="github.com/DaRkSurface"))
          print(f'{Fore.LIGHTGREEN_EX}Logged in as: {Fore.YELLOW}"{bot.user}" {Fore.LIGHTGREEN_EX}| ID: {Fore.YELLOW}"{bot.user}"{Fore.LIGHTGREEN_EX}\nConnected with {Fore.YELLOW}{len(bot.guilds)}{Fore.LIGHTGREEN_EX} Guilds and {Fore.YELLOW}{len(bot.user.friends)} {Fore.LIGHTGREEN_EX}Friends')
          print(f'{Fore.LIGHTYELLOW_EX}[+] Started sending DMs to the IDs\n')
          await massdm()
      elif send_embed == "True":
          await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="github.com/DaRkSurface"))
          print(f'{Fore.LIGHTGREEN_EX}Logged in as: {Fore.YELLOW}"{bot.user}" {Fore.LIGHTGREEN_EX}| ID: {Fore.YELLOW}"{bot.user}"{Fore.LIGHTGREEN_EX}\nConnected with {Fore.YELLOW}{len(bot.guilds)}{Fore.LIGHTGREEN_EX} Guilds and {Fore.YELLOW}{len(bot.user.friends)} {Fore.LIGHTGREEN_EX}Friends')
          print(f'{Fore.LIGHTYELLOW_EX}[+] Started sending Embed Messages to the IDs\n')
          await massdmembed()
      else:
          print(f"{Fore.RED} EMBED ERROR")
          error_msg()
  try:
      bot.run(token, bot=False)
  except Exception as ex:
      print(f"{Fore.RED}TOKEN ERROR - {ex}")
      print(token)
      time.sleep(10)

  
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
  [5] Selfbot (Not Stable)

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
    clearcmd()
    massdm()
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

def selfbot():
  pass


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
