#!/usr/bin/python3

#####################################################
## DarkDiscord (DrkDC)                             ##
## A useful tool to gen/check discord stuff        ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
## NOTE: some parts are skidded due to laziness.   ##
#####################################################

# Imports
import json
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
import asyncio
import sys
try:
  import discum
except ImportError:
  try:
      subprocess.check_call([sys.executable, "-m", "pip", "install", '--user', "--upgrade",
                             "git+https://github.com/Merubokkusu/Discord-S.C.U.M#egg=discum"])
  except:
      subprocess.check_call([sys.executable, "-m", "pip", "install", 'discum'])


# Global Variables
drk = 14


# Defines
def error_msg():
    print(pyfade.Fade.Horizontal(pyfade.Colors.purple_to_red, """Error bro, Error.. I wonder why?!"""))

def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')


def massdm():
  def error_msg():
      print(pyfade.Fade.Horizontal(pyfade.Colors.purple_to_red, """Error bro, error ):"""))
      time.sleep(5)
      input(f"{Fore.YELLOW}Press Enter to exit the script")
      raise SystemExit
  sys.tracebacklimit = 0
  bot = discord.Client()
  with open("./selfbot/tokens.json", "r") as file:
      tokens = json.load(file)
  with open("./selfbot/usedtokens.json", "r") as file:
      tokenscheck = json.load(file)
  unused_tokens = []
  if len(tokens) == 0:
      print("No Tokens were found\nScript is closing")
      raise SystemExit
  for tkn in tokens:
      if tkn in tokenscheck:
          pass
      else:
          unused_tokens.append(tkn)
  if len(unused_tokens) != 0:
      token = random.choice(unused_tokens)
      tokenscheck.append(token)
      with open("./selfbot/usedtokens.json", "w", encoding='utf-8') as file:
          json.dump(tokenscheck, file)
  else:
    reset = []
    with open('./selfbot/alrdyusedtokens.json', 'w', encoding='utf-8') as f:
        json.dump(reset, f, ensure_ascii=False, indent=4)
    print(f"{Fore.RED}Resetting already used tokens for the selfbot, you may have to restart the script.")
    time.sleep(5) 

  with open('./selfbot/config.json') as f:
      yamete_kudasai = json.load(f)
  cooldown = yamete_kudasai['min_cooldown']
  cooldown_max = yamete_kudasai['max_cooldown']
  display_sleep = yamete_kudasai['display_sleep']
  message = yamete_kudasai['message']
  dm_limit = yamete_kudasai['dm_each_token']
  always_sleep = yamete_kudasai['sleep_on_exception']
  duplicate = yamete_kudasai['dm_already_dmed_users']
  fetch_users = yamete_kudasai['always_fetch_users']
  send_embed = yamete_kudasai['send_embed']
  embed_title = yamete_kudasai['embed_title']
  embed_description = yamete_kudasai['embed_description']
  embed_author = yamete_kudasai['embed_author']
  embed_footer = yamete_kudasai['embed_footer']
  embed_footer_icon_url = yamete_kudasai['embed_footer_icon_url']
  embed_thumbnail_url = yamete_kudasai['embed_thumbnail_url']
  embed_image_url = yamete_kudasai['embed_image_url']
  embed_author_icon_url = yamete_kudasai['embed_author_icon_url']
  if duplicate == "True":
      munanyo = "True"
  elif duplicate == "False":
      munanyo = "False"
  else:
      munanyo = "False"
  async def mass_dm():
      with open("./selfbot/id.json", "r", encoding='utf-8') as file:
          data = json.load(file)
      with open("./selfbot/blacklistedid.json", "r", encoding='utf-8') as file:
          blcklstdata = json.load(file)
      indx = 0
      success = 0
      for i in data:
          with open("./selfbot/usedids.json", "r", encoding='utf-8') as file:
              penis = json.load(file)
          now = datetime.now()
          current_time = now.strftime("%H:%M")
          indx += 1
          if int(i) in blcklstdata:
              if fetch_users == "False":
                  print(f"{Fore.BLUE}{current_time} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{i} {Fore.BLACK}{indx} / {len(data)}")
              elif fetch_users == "True":
                  chupapi = await bot.fetch_user(i)
                  print(f"{Fore.BLUE}{current_time} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{chupapi} {Fore.BLACK}{indx} / {len(data)}")
                  print(f"{Fore.YELLOW}Sleeping 2 seconds")
                  await asyncio.sleep(2)
              else:
                  print(f"{Fore.RED}[FETCH USERS ERROR]")
                  error_msg()
          elif munanyo == "False":
              if int(i) in penis:
                  if fetch_users == "False":
                      print(f"{Fore.BLUE}{current_time} {Fore.LIGHTMAGENTA_EX}[x] Avoiding Duplicates: {Fore.YELLOW}{i} {Fore.BLACK}{indx} / {len(data)}")
                  elif fetch_users == "True":
                      chupapi = await bot.fetch_user(i)
                      print(f"{Fore.BLUE}{current_time} {Fore.LIGHTMAGENTA_EX}[x] Avoiding Duplicates: {Fore.YELLOW}{chupapi} {Fore.BLACK}{indx} / {len(data)}")
                      print(f"{Fore.YELLOW}Sleeping 2 seconds")
                      await asyncio.sleep(2)
                  else:
                      print(f"{Fore.RED}[FETCH USERS ERROR]")
                      error_msg()
              else:
                  chupapi = await bot.fetch_user(i)
                  try:
                      await chupapi.send(message.replace('user_id', f'{chupapi.id}').replace('user_name', f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator', f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'))
                      print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[+] Sent {message} to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
                      pablo = random.randint(cooldown, cooldown_max)
                      success += 1
                      if success >= dm_limit:
                          print(f"{Fore.BLUE}{current_time} {Fore.LIGHTCYAN_EX}[?] DM Limit has been reached: {Fore.YELLOW}{dm_limit} DMs {Fore.LIGHTCYAN_EX}(Switching the token in 1 second)")
                          await asyncio.sleep(1)
                          os.execv(sys.executable, ['python'] + sys.argv)
                      if display_sleep == "True":
                            print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                      else:
                          pass
                      await asyncio.sleep(pablo)
                  except discord.Forbidden as e:
                      if e.code == 40003:
                          print(
                              f"{Fore.LIGHTYELLOW_EX} You have been Rate Limited\nThe Code will be restarted in 90 seconds - {Fore.RED}{e}")
                          await asyncio.sleep(90)
                          os.execv(sys.executable, ['python'] + sys.argv)
                          continue
                      else:
                          print(
                              f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")
                          pablo = random.randint(cooldown, cooldown_max)
                          if always_sleep == "True":
                              if display_sleep == "True":
                                  print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                              await asyncio.sleep(pablo)
                  except discord.HTTPException as e:
                      print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t fetch {Fore.YELLOW}{i}{Fore.RED} - {e} {indx} / {len(data)}")
                  if chupapi.id not in penis:
                      await asyncio.sleep(0.01)
                      penis.append(chupapi.id)
                      with open("./selfbot/usedids.json", "w") as file:
                          await asyncio.sleep(0.01)
                          json.dump(penis, file)
          else:
              try:
                  chupapi = await bot.fetch_user(i)
                  await chupapi.send(message.replace('user_id', f'{chupapi.id}').replace('user_name', f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator', f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'))
                  print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[+] Sent {message} to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
                  pablo = random.randint(cooldown, cooldown_max)
                  success += 1
                  if success >= dm_limit:
                      print(f"{Fore.BLUE}{current_time} {Fore.LIGHTCYAN_EX}[?] DM Limit has been reached: {Fore.YELLOW}{dm_limit} DMs {Fore.LIGHTCYAN_EX}(Switching the token in 1 second)")
                      await asyncio.sleep(1)
                      os.execv(sys.executable, ['python'] + sys.argv)
                  if display_sleep == "True":
                      print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                  else:
                      pass
                  await asyncio.sleep(pablo)
              except discord.Forbidden as e:
                  if e.code == 40003:
                      print(f"{Fore.LIGHTYELLOW_EX}You have been Rate Limited\nThe Code will be restarted in 90 seconds - {Fore.RED}{e}")
                      await asyncio.sleep(90)
                      os.execv(sys.executable, ['python'] + sys.argv)
                      continue
                  else:
                      print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")
                      pablo = random.randint(cooldown, cooldown_max)
                      if always_sleep == "True":
                          if display_sleep == "True":
                              print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                          await asyncio.sleep(pablo)
              except discord.HTTPException as e:
                  print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t fetch {Fore.YELLOW}{i}{Fore.RED} - {e} {indx} / {len(data)}")
              if chupapi.id not in penis:
                  penis.append(chupapi.id)
                  with open("./selfbot/usedids.json", "w") as file:
                      json.dump(penis, file)
      input(f"{Fore.LIGHTGREEN_EX}Press Enter 5 times to close the program.")
      [input(i) for i in range(4, 0, -1)]
      print("Goodbye!\nhttps://github.com/DaRkSurface/drkdiscord")
      await sys.exit()
  async def mass_dm_embed():
      with open("./selfbot/id.json", "r", encoding='utf-8') as file:
          data = json.load(file)
      with open("./selfbot/blacklistedid.json", "r", encoding='utf-8') as file:
          blcklstdata = json.load(file)
      indx = 0
      success = 0
      for i in data:
          with open("./selfbot/usedids.json", "r", encoding='utf-8') as file:
              penis = json.load(file)
          now = datetime.now()
          current_time = now.strftime("%H:%M")
          indx += 1
          if int(i) in blcklstdata:
              if fetch_users == "False":
                  print(f"{Fore.BLUE}{current_time} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{i} {Fore.BLACK}{indx} / {len(data)}")
              elif fetch_users == "True":
                  chupapi = await bot.fetch_user(i)
                  print(f"{Fore.BLUE}{current_time} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{chupapi} {Fore.BLACK}{indx} / {len(data)}")
                  print(f"{Fore.YELLOW}Sleeping 2 seconds")
                  await asyncio.sleep(2)
              else:
                  print(f"{Fore.RED}[FETCH USERS ERROR]")
                  error_msg()
          elif munanyo == "False":
              if int(i) in penis:
                  if fetch_users == "False":
                      print(f"{Fore.BLUE}{current_time} {Fore.LIGHTMAGENTA_EX}[x] Avoiding Duplicates: {Fore.YELLOW}{i} {Fore.BLACK}{indx} / {len(data)}")
                  elif fetch_users == "True":
                      chupapi = await bot.fetch_user(i)
                      print(f"{Fore.BLUE}{current_time} {Fore.LIGHTMAGENTA_EX}[x] Avoiding Duplicates: {Fore.YELLOW}{chupapi} {Fore.BLACK}{indx} / {len(data)}")
                      print(f"{Fore.YELLOW}Sleeping 2 seconds")
                      await asyncio.sleep(2)
                  else:
                      print(f"{Fore.RED}[FETCH USERS ERROR]")
                      error_msg()
              else:
                  chupapi = await bot.fetch_user(i)
                  embed_skrr = discord.Embed(title=f"{embed_title}".replace('user_id', f'{chupapi.id}').replace('user_name', f'{chupapi.name}').replace('user_discriminator', f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'),icon_url=embed_footer_icon_url.replace('user_avatar', f'{chupapi.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}'),description=f"{embed_description}".replace('user_id', f'{chupapi.id}').replace('user_name',f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator',f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'), color=discord.Colour.random())
                  embed_skrr.set_thumbnail(url=f"{embed_thumbnail_url}"), embed_skrr.set_image(url=f"{embed_image_url}"), embed_skrr.set_author(name=f"{embed_author}".replace('user_id', f'{chupapi.id}').replace('user_name',f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator',f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'), icon_url=embed_author_icon_url.replace('user_avatar',f'{chupapi.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}')), embed_skrr.set_footer(text=f"{embed_footer}".replace('user_id', f'{chupapi.id}').replace('user_name',f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator',f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'),icon_url=embed_footer_icon_url.replace('user_avatar',f'{chupapi.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}'))
                  try:
                      await chupapi.send(embed=embed_skrr)
                      print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[+] Sent the embed to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
                      pablo = random.randint(cooldown, cooldown_max)
                      success += 1
                      if success >= dm_limit:
                          print(f"{Fore.BLUE}{current_time} {Fore.LIGHTCYAN_EX}[?] DM Limit has been reached: {Fore.YELLOW}{dm_limit} DMs {Fore.LIGHTCYAN_EX}(Switching the token in 1 second)")
                          await asyncio.sleep(1)
                          os.execv(sys.executable, ['python'] + sys.argv)
                      if display_sleep == "True":
                            print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                      else:
                          pass
                      await asyncio.sleep(pablo)
                  except discord.Forbidden as e:
                      if e.code == 40003:
                          print(f"{Fore.LIGHTYELLOW_EX}You have been Rate Limited\nThe Code will be restarted in 90 seconds - {Fore.RED}{e}")
                          await asyncio.sleep(90)
                          os.execv(sys.executable, ['python'] + sys.argv)
                          continue
                      else:
                          print(
                              f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")
                          pablo = random.randint(cooldown, cooldown_max)
                          if always_sleep == "True":
                              if display_sleep == "True":
                                  print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                              await asyncio.sleep(pablo)
                  except discord.HTTPException as e:
                      print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t fetch {Fore.YELLOW}{i}{Fore.RED} - {e} {indx} / {len(data)}")
                  if chupapi.id not in penis:
                      penis.append(chupapi.id)
                      with open("./selfbot/usedids.json", "w") as file:
                          json.dump(penis, file)
          else:
              try:
                  chupapi = await bot.fetch_user(i)
                  embed_skrr = discord.Embed(title=f"{embed_title}".replace('user_id', f'{chupapi.id}').replace('user_name',f'{chupapi.name}').replace('user_discriminator', f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'),icon_url=embed_footer_icon_url.replace('user_avatar',f'{chupapi.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}'), description=f"{embed_description}".replace('user_id', f'{chupapi.id}').replace('user_name',f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator', f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'), color=discord.Colour.random())
                  embed_skrr.set_thumbnail(url=f"{embed_thumbnail_url}"), embed_skrr.set_image(url=f"{embed_image_url}"), embed_skrr.set_author(name=f"{embed_author}".replace('user_id', f'{chupapi.id}').replace('user_name',f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator',f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'), icon_url=embed_author_icon_url.replace('user_avatar',f'{chupapi.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}')), embed_skrr.set_footer(text=f"{embed_footer}".replace('user_id', f'{chupapi.id}').replace('user_name',f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator',f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'),icon_url=embed_footer_icon_url.replace('user_avatar',f'{chupapi.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}'))
                  await chupapi.send(embed=embed_skrr)
                  print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[+] Sent the embed to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
                  success +=1
                  if success >= dm_limit:
                      print(f"{Fore.BLUE}{current_time} {Fore.LIGHTCYAN_EX}[?] DM Limit has been reached: {Fore.YELLOW}{dm_limit} DMs {Fore.LIGHTCYAN_EX}(Switching the token in 1 second)")
                      await asyncio.sleep(1)
                      os.execv(sys.executable, ['python'] + sys.argv)
                  pablo = random.randint(cooldown, cooldown_max)
                  if display_sleep == "True":
                      print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                  else:
                      pass
                  await asyncio.sleep(pablo)
              except discord.Forbidden as e:
                  if e.code == 40003:
                      print(f"{Fore.LIGHTYELLOW_EX}You have been Rate Limited\nThe Code will be restarted in 90 seconds - {Fore.RED}{e}")
                      await asyncio.sleep(90)
                      os.execv(sys.executable, ['python'] + sys.argv)
                      continue
                  else:
                      print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")
                      pablo = random.randint(cooldown, cooldown_max)
                      if always_sleep == "True":
                          if display_sleep == "True":
                              print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                          await asyncio.sleep(pablo)
              except discord.HTTPException as e:
                  print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t fetch {Fore.YELLOW}{i}{Fore.RED} - {e} {indx} / {len(data)}")
              if chupapi.id not in penis:
                  penis.append(chupapi.id)
                  with open("./selfbot/usedids.json", "w") as file:
                      json.dump(penis, file)
      input(f"{Fore.LIGHTGREEN_EX}Press Enter 5 times to close the program.")
      [input(i) for i in range(4, 0, -1)]
      print("Goodbye!\nhttps://github.com/DaRkSurface")
      back()
      clearcmd()
      options()

  print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_cyan, '''
    DRK DISCORD Alpha (V0.9)
  ██████╗ ██████╗ ██╗  ██╗    ███╗   ███╗ █████╗ ███████╗███████╗    ██████╗ ███╗   ███╗
  ██╔══██╗██╔══██╗██║ ██╔╝    ████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔══██╗████╗ ████║
  ██║  ██║██████╔╝█████╔╝     ██╔████╔██║███████║███████╗███████╗    ██║  ██║██╔████╔██║
  ██║  ██║██╔══██╗██╔═██╗     ██║╚██╔╝██║██╔══██║╚════██║╚════██║    ██║  ██║██║╚██╔╝██║
  ██████╔╝██║  ██║██║  ██╗    ██║ ╚═╝ ██║██║  ██║███████║███████║    ██████╔╝██║ ╚═╝ ██║
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚═╝     ╚═╝
                                                                                      '''))
  print(f'''{Fore.LIGHTWHITE_EX}                                             PART OF: {Fore.YELLOW}DRK DISCORD 
  {Fore.RED}MAJORITY OF THIS CODE IS FROM hoemotion (https://gihub.com/hoemotion) {Fore.LIGHTBLUE_EX}forked in: https://github.com/DaRkSurface 
  ''')
  time.sleep(1.5)
  @bot.event
  async def on_ready():
      if send_embed == "False":
          await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="github.com/DaRkSurface"))
          print(f'{Fore.LIGHTGREEN_EX}Logged in as: {Fore.YELLOW}"{bot.user}" {Fore.LIGHTGREEN_EX}| ID: {Fore.YELLOW}"{bot.user}"{Fore.LIGHTGREEN_EX}\nConnected with {Fore.YELLOW}{len(bot.guilds)}{Fore.LIGHTGREEN_EX} Guilds and {Fore.YELLOW}{len(bot.user.friends)} {Fore.LIGHTGREEN_EX}Friends')
          print(f'{Fore.LIGHTYELLOW_EX}[⚡] Started sending DMs to the IDs\n')
          await mass_dm()
      elif send_embed == "True":
          await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="github.com/DaRkSurface"))
          print(f'{Fore.LIGHTGREEN_EX}Logged in as: {Fore.YELLOW}"{bot.user}" {Fore.LIGHTGREEN_EX}| ID: {Fore.YELLOW}"{bot.user}"{Fore.LIGHTGREEN_EX}\nConnected with {Fore.YELLOW}{len(bot.guilds)}{Fore.LIGHTGREEN_EX} Guilds and {Fore.YELLOW}{len(bot.user.friends)} {Fore.LIGHTGREEN_EX}Friends')
          print(f'{Fore.LIGHTYELLOW_EX}[⚡] Started sending Embed Messages to the IDs\n')
          await mass_dm_embed()
      else:
          print(f"{Fore.RED} EMBED ERROR")
          error_msg()
  try:
      bot.run(token, bot=False)
  except Exception as e:
      print(f"{Fore.RED}TOKEN ERROR - {e} \n If this keeps happening try and remove the json contents in usedtokens.json")
      print(token)
      time.sleep(10)
      os.execv(sys.executable, ['python'] + sys.argv)

def id_logger():
    sys.tracebacklimit = 0
    with open('./selfbot/config.json') as f:
        yamete_kudasai = json.load(f)
    token = yamete_kudasai['token']
    whitelist = "False"
    print(pyfade.Fade.Horizontal(pyfade.Colors.cyan_to_blue, '''
     DRK DISCORD Alpth (V0.5)
    ██╗██████╗         ██╗      █████╗  ██████╗  ██████╗ ███████╗██████╗ 
    ██║██╔══██╗        ██║     ██╔══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
    ██║██║  ██║        ██║     ██║  ██║██║  ██╗ ██║  ██╗ █████╗  ██████╔╝
    ██║██║  ██║        ██║     ██║  ██║██║  ╚██╗██║  ╚██╗██╔══╝  ██╔══██╗
    ██║██████╔╝        ███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
    ╚═╝╚═════╝         ╚══════╝ ╚════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝'''))
    print(f'''{Fore.LIGHTWHITE_EX}                                             PART OF: {Fore.YELLOW}DRK DISCORD 
    {Fore.RED}MAJORITY OF THIS CODE IS FROM hoemotion (https://gihub.com/hoemotion) {Fore.LIGHTBLUE_EX}forked in: https://github.com/DaRkSurface 
    ''')

    def log_id(reason, id, name, discriminator, guild):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        try:
            with open("./selfbot/blacklistedid.json", "r") as file:
                data = json.load(file)
                if id not in data:
                    pass
                elif id in data:
                    return

            with open("./selfbot/id.json", "r") as file:
                data = json.load(file)
                time.sleep(0.01)

            if id not in data:
                time.sleep(0.01)
                data.append(id)

                with open("./selfbot/id.json", "w") as file:
                    time.sleep(0.01)
                    json.dump(data, file)

                try:
                    print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[{Fore.YELLOW}{guild}{Fore.LIGHTGREEN_EX} | {Fore.YELLOW}{reason}{Fore.LIGHTGREEN_EX}] {Fore.YELLOW}{name}#{discriminator} {Fore.LIGHTGREEN_EX}- {Fore.YELLOW}{id}{Fore.LIGHTGREEN_EX} Total:{Fore.YELLOW} {len(data)}")
                except AttributeError:
                    print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[{Fore.YELLOW}{reason}{Fore.LIGHTGREEN_EX}]{Fore.YELLOW} {name}#{discriminator} {Fore.LIGHTGREEN_EX}- {Fore.YELLOW}{id} {Fore.LIGHTGREEN_EX}Total: {Fore.YELLOW}{len(data)}")
                except:
                    pass

        except:
            pass

    bot = discord.Client()

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="github.com/DaRkSurface"))
        await bot.change_presence(status=discord.Status.idle)
        print(f'{Fore.LIGHTGREEN_EX}Logged in as: {Fore.YELLOW}"{bot.user}" {Fore.LIGHTGREEN_EX}| ID: {Fore.YELLOW}"{bot.user.id}"{Fore.LIGHTGREEN_EX}\nConnected with {Fore.YELLOW}{len(bot.guilds)}{Fore.LIGHTGREEN_EX} Guilds and {Fore.YELLOW}{len(bot.user.friends)} {Fore.LIGHTGREEN_EX}Friends')
        print(f'{Fore.LIGHTYELLOW_EX}[⚡] Started logging IDs\n')
        if len(bot.guilds) < 20:
            print("Logging IDs will become faster if you join more Servers!")

    @bot.event
    async def on_message(message):
        if whitelist == "True":
            with open('./selfbot/whitelistedservers.json') as f:
                whitlisted_servers = json.load(f)
            if message.guild.id in whitlisted_servers:
                await asyncio.sleep(0.1)
                try:
                    with open('./selfbot/blacklistedservers.json') as f:
                        banned_servers = json.load(f)
                    if message.guild.id in banned_servers:
                        return
                    else:
                        pass
                    try:
                        if not message.author.bot:
                            try:
                                reason = "MESSAGE"
                                log_id(message.author.id, message.author.name, message.author.discriminator,
                                    message.author.guild, reason)
                            except AttributeError:
                                pass

                        if message.author.bot:
                            pass
                    except AttributeError:
                        pass
                except:
                    pass
            else:
                return
        else:
            await asyncio.sleep(0.1)
            try:
                with open('./selfbot/blacklistedservers.json') as f:
                    banned_servers = json.load(f)
                if message.guild.id in banned_servers:
                    return
                else:
                    pass
                try:
                    if not message.author.bot:
                        try:
                            reason = "MESSAGE"
                            log_id(reason, message.author.id, message.author.name, message.author.discriminator,
                                message.author.guild)
                        except AttributeError:
                            pass

                    if message.author.bot:
                        pass
                except AttributeError:
                    pass
            except:
                pass

    @bot.event
    async def on_delete(message):
        if whitelist == "True":
            with open('./selfbot/whitelistedservers.json', "r") as f:
                whitlisted_servers = json.load(f)
            if message.guild.id in whitlisted_servers:
                await asyncio.sleep(0.1)
                try:
                    with open('./selfbot/blacklistedservers.json', "r") as f:
                        banned_servers = json.load(f)
                    if message.guild.id in banned_servers:
                        return
                    else:
                        pass
                        try:
                            if not message.author.bot:
                                reason = "MESSAGE DELETED"
                                log_id(reason, message.author.id, message.author.name, message.author.discriminator,
                                    message.author.guild)
                            if message.author.bot:
                                pass
                        except AttributeError:
                            pass
                except:
                    pass
            else:
                pass
        else:
            await asyncio.sleep(0.1)
            try:
                with open('./selfbot/blacklistedservers.json', "r") as f:
                    banned_servers = json.load(f)
                if message.guild.id in banned_servers:
                    return
                else:
                    pass
                    try:
                        if not message.author.bot:
                            reason = "MESSAGE DELETED"
                            log_id(reason, message.author.id, message.author.name, message.author.discriminator,
                                message.author.guild)
                        if message.author.bot:
                            pass
                    except AttributeError:
                        pass
            except:
                pass

    @bot.event
    async def on_raw_reaction_add(payload):
        if whitelist == "True":
            with open('./selfbot/whitelistedservers.json', "r") as f:
                whitlisted_servers = json.load(f)
            if payload.member.guild.id in whitlisted_servers:
                await asyncio.sleep(0.1)
                try:
                    with open('./selfbot/blacklistedservers.json', "r") as f:
                        banned_servers = json.load(f)
                    if payload.member.guild.id in banned_servers:
                        return
                    else:
                        pass
                    try:
                        if not payload.member.bot:
                            reason = "EMOJI REACTION (RAW)"
                            log_id(reason, payload.member.id, payload.member.name, payload.member.discriminator,
                                payload.member.guild)
                    except:
                        pass
                except:
                    pass
            else:
                return
        else:
            await asyncio.sleep(0.1)
            try:
                with open('./selfbot/blacklistedservers.json', "r") as f:
                    banned_servers = json.load(f)
                if payload.member.guild.id in banned_servers:
                    return
                else:
                    pass
                try:
                    if not payload.member.bot:
                        reason = "EMOJI REACTION (RAW)"
                        log_id(reason, payload.member.id, payload.member.name, payload.member.discriminator,
                            payload.member.guild)
                except:
                    pass
            except:
                pass


    @bot.event
    async def on_edit(message):
        if whitelist == "True":
            with open('./selfbot/whitelistedservers.json', "r") as f:
                whitlisted_servers = json.load(f)
            if message.guild.id in whitlisted_servers:
                await asyncio.sleep(0.1)
                try:
                    with open('./selfbot/blacklistedservers.json', "r") as f:
                        banned_servers = json.load(f)
                    if message.guild.id in banned_servers:
                        return
                    else:
                        pass
                        try:
                            if not message.author.bot:
                                reason = "MESSAGE EDIT"
                                log_id(reason, message.author.id, message.author.name, message.author.discriminator,
                                    message.author.guild)
                            if message.author.bot:
                                pass
                        except AttributeError:
                            pass
                except:
                    pass
            else:
                return
        else:
            await asyncio.sleep(0.1)
            try:
                with open('./selfbot/blacklistedservers.json', "r") as f:
                    banned_servers = json.load(f)
                if message.guild.id in banned_servers:
                    return
                else:
                    pass
                    try:
                        if not message.author.bot:
                            reason = "MESSAGE EDIT"
                            log_id(reason, message.author.id, message.author.name, message.author.discriminator,
                                message.author.guild)
                        if message.author.bot:
                            pass
                    except AttributeError:
                        pass
            except:
                pass

    @bot.event
    async def on_member_join(member):
        if whitelist == "True":
            with open('./selfbot/whitelistedservers.json', "r") as f:
                whitlisted_servers = json.load(f)
            if member.guild.id in whitlisted_servers:
                await asyncio.sleep(0.1)
                try:
                    with open('./selfbot/blacklistedservers.json', "r") as f:
                        banned_servers = json.load(f)
                    if member.guild.id in banned_servers:
                        return
                    else:
                        pass
                        try:
                            if not member.bot:
                                reason = "GUILD JOIN"
                                log_id(reason, member.id, member.name, member.discriminator, member.guild)
                            if member.bot:
                                pass
                        except AttributeError:
                            pass
                except:
                    pass
            else:
                return
        else:
            await asyncio.sleep(0.1)
            try:
                with open('./selfbot/blacklistedservers.json', "r") as f:
                    banned_servers = json.load(f)
                if member.guild.id in banned_servers:
                    return
                else:
                    pass
                    try:
                        if not member.bot:
                            reason = "GUILD JOIN"
                            log_id(reason, member.id, member.name, member.discriminator, member.guild)
                        if member.bot:
                            pass
                    except AttributeError:
                        pass
            except:
                pass

    @bot.event
    async def on_member_remove(user):
        if whitelist == "True":
            with open('./selfbot/whitelistedservers.json', "r") as f:
                whitlisted_servers = json.load(f)
            if user.guild.id in whitlisted_servers:
                await asyncio.sleep(0.1)
                try:
                    with open('./selfbot/blacklistedservers.json', "r") as f:
                        banned_servers = json.load(f)
                    if user.guild.id in banned_servers:
                        return
                    else:
                        pass
                        try:
                            if not user.bot:
                                reason = "GUILD LEAVE"
                                log_id(reason, user.id, user.name, user.discriminator, user.guild)
                            if user.bot:
                                pass
                        except AttributeError:
                            pass
                except:
                    pass
            else:
                return
        else:
            await asyncio.sleep(0.1)
            try:
                with open('./selfbot/blacklistedservers.json', "r") as f:
                    banned_servers = json.load(f)
                if user.guild.id in banned_servers:
                    return
                else:
                    pass
                    try:
                        if not user.bot:
                            reason = "GUILD LEAVE"
                            log_id(reason, user.id, user.name, user.discriminator, user.guild)
                        if user.bot:
                            pass
                    except AttributeError:
                        pass
            except:
                pass

    @bot.event
    async def on_member_update(before, after):
        if whitelist == "True":
            with open('./selfbot/whitelistedservers.json', "r") as f:
                whitlisted_servers = json.load(f)
            if before.member.guild.id in whitlisted_servers:
                await asyncio.sleep(0.1)
                try:
                    with open('./selfbot/blacklistedservers.json', "r") as f:
                        banned_servers = json.load(f)
                    if after.member.guild.id in banned_servers:
                        return
                    else:
                        pass
                        try:
                            if not after.member.bot:
                                reason = "MEMBER UPDATE"
                                log_id(reason, after.member.id, after.member.name, after.member.discriminator,
                                    after.member.guild)
                            if after.member.bot:
                                pass
                        except AttributeError:
                            pass
                except:
                    pass
            else:
                return
        else:
            await asyncio.sleep(0.1)
            try:
                with open('./selfbot/blacklistedservers.json', "r") as f:
                    banned_servers = json.load(f)
                if after.member.guild.id in banned_servers:
                    return
                else:
                    pass
                    try:
                        if not after.member.bot:
                            reason = "MEMBER UPDATE"
                            log_id(reason, after.member.id, after.member.name, after.member.discriminator, after.member.guild)
                        if after.member.bot:
                            pass
                    except AttributeError:
                        pass
            except:
                pass

    @bot.event
    async def on_voice_state_update(member, before, after):
        if whitelist == "True":
            with open('./selfbot/whitelistedservers.json', "r") as f:
                whitlisted_servers = json.load(f)
            if before.member.guild.id in whitlisted_servers:
                await asyncio.sleep(0.1)
                try:
                    with open('./selfbot/blacklistedservers.json', "r") as f:
                        banned_servers = json.load(f)
                    if after.member.guild.id in banned_servers:
                        return
                    else:
                        pass
                        try:
                            if not member.bot:
                                reason = "VOICE STATE UPDATE"
                                log_id(reason, member.id, member.name, member.discriminator, member.guild)
                            if member.bot:
                                pass
                        except AttributeError:
                            pass
                except:
                    pass
            else:
                return
        else:
            await asyncio.sleep(0.1)
            try:
                with open('./selfbot/blacklistedservers.json', "r") as f:
                    banned_servers = json.load(f)
                if after.member.guild.id in banned_servers:
                    return
                else:
                    pass
                    try:
                        if not member.bot:
                            reason = "VOICE STATE UPDATE"
                            log_id(reason, member.id, member.name, member.discriminator, member.guild)
                        if member.bot:
                            pass
                    except AttributeError:
                        pass
            except:
                pass

    @bot.event
    async def on_reaction_add(reaction, member):
        if whitelist == "True":
            with open('./selfbot/whitelistedservers.json', "r") as f:
                whitlisted_servers = json.load(f)
            if member.guild.id in whitlisted_servers:
                await asyncio.sleep(0.1)
                try:
                    with open('./selfbot/blacklistedservers.json', "r") as f:
                        banned_servers = json.load(f)
                    if member.guild.id in banned_servers:
                        return
                    else:
                        pass
                        try:
                            if not member.bot:
                                reason = "EMOJI REACTION"
                                log_id(reason, member.id, member.name, member.discriminator, member.guild)
                            if member.bot:
                                pass
                        except AttributeError:
                            pass
                except:
                    pass
            else:
                return
        await asyncio.sleep(0.1)
        try:
            with open('./selfbot/blacklistedservers.json', "r") as f:
                banned_servers = json.load(f)
            if member.guild.id in banned_servers:
                return
            else:
                pass
                try:
                    if not member.bot:
                        reason = "EMOJI REACTION"
                        log_id(reason, member.id, member.name, member.discriminator, member.guild)
                    if member.bot:
                        pass
                except AttributeError:
                    pass
        except:
            pass
    try:
        bot.run(token, bot=False)
    except Exception as e:
        print(f"{Fore.RED}TOKEN ERROR - {e}")
        error_msg()

def self_bot():
  test = True
  if test == True:

    print(pyfade.Fade.Horizontal(pyfade.Colors.red_to_blue, """
     DRK DISCORD Alpha (V0.9)
  ██████╗ ██████╗ ██╗  ██╗    ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
  ██╔══██╗██╔══██╗██║ ██╔╝    ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
  ██║  ██║██████╔╝█████╔╝     ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
  ██║  ██║██╔══██╗██╔═██╗     ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
  ██████╔╝██║  ██║██║  ██╗    ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   
                                                                                        
      
    \n"""))

    print("""
  [1] Mass DM Spammer
  [2] Id Logger (Do this before Mass DMing)
  [3] Coming soon.

  [4] Go back
    
    """)
    USER_OPT = input("Option\n> ")
    if USER_OPT == "1":
      clearcmd()
      massdm()
    elif USER_OPT == "2":
      clearcmd()
      id_logger()
    elif USER_OPT == "3":
      underdev()
      back()
      clearcmd()
      self_bot()
    elif USER_OPT == "4":
      print(f"{Fore.RED}Going back.")
      time.sleep(0.3)
      clearcmd()
      options()
    else:
      print(f"{Fore.RED}[-] Did not reckognize {Fore.YELLOW}{USER_OPT}{Fore.YELLOW} Watch if you have hidden spaces!")
      back()
      clearcmd()
      self_bot()
    

def banner():
  print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_red, """
   V. 0.9 Alpha (January 10th 2022)
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
  [3] Nitro Gift/Code Generator
  [4] Nitro Gift/Code Checker (Not Stable)
  [5] Selfbot Options (Not Stable)

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
    self_bot()
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
   DRK DISCORD Alpha (V0.9)
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
  randomgift = "https://discord.gift/CwyBhRjAsnGw6GzCkgE56NVW"
  characters = "abcdefghijklmnopqrstuwyxzABCDEFGHIJKLMNOPQRSTUWYXZ1234567890"
  
  print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_cyan, """
   DRK DISCORD Alpha (V0.9)
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
  print(f"""{Fore.LIGHTWHITE_EX}

  LIST

  [1] Promotion Gift Code (24 chars)
  [2] Discord User Gift Code (16 chars)
  
  """)
  which = input(f"{Fore.YELLOW}Option\n> ")
  if which == "1":
    with open("./generated/nitro/nitro.txt", "w+") as file:
        file.write("##THESE ARE SUPPOSED TO BE USED IN THE CHECKER!!")
        file.write("\n")
        for i in range(int(howmany)):
            genrandom = ''.join(random.choice(characters) for i in range(24))
            file.write(genrandom)
            file.write("\n")
        print(f"\n{Fore.YELLOW}[*] Generating... \n")
        time.sleep(2)
        print(f"{Fore.GREEN}[+] Generated {Fore.RED}{howmany}{Fore.GREEN} Discord Nitro Gift Links(s). Saved to ./generated/nitro/nitro.txt ")
  elif which == "2":
    with open("./generated/nitro/nitro.txt", "w+") as file:
        for i in range(int(howmany)):
            genrandom = ''.join(random.choice(characters) for i in range(16))
            file.write(genrandom)
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
   DRK DISCORD Alpha (0.9)
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
    elif response.status_code == 10038: 
        return False
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
