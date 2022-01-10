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
    pass # Due to bug

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
  {Fore.RED}THIS SCRIPT IS SKIDDED FROM hoemotion (https://gihub.com/hoemotion) {Fore.LIGHTBLUE_EX}forked in: https://github.com/DaRkSurface 
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
      print(f"{Fore.RED}TOKEN ERROR - {e}")
      print(token)
      time.sleep(10)
      os.execv(sys.executable, ['python'] + sys.argv)

def idscraper():

  start = time.time()

  with open('./selfbot/config.json') as f:
      yamete_kudasai = json.load(f)
  token = yamete_kudasai['token']
  bot = discum.Client(token=token)

  def close_after_fetching(resp, guild_id):
      if bot.gateway.finishedMemberFetching(guild_id):
          lenmembersfetched = len(bot.gateway.session.guild(guild_id).members) #this line is optional
          print(str(lenmembersfetched)+' members fetched') #this line is optional
          bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
          bot.gateway.close()

  def get_members(guild_id, channel_id):
      bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1) #get all user attributes, wait 1 second between requests
      bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
      bot.gateway.run()
      bot.gateway.resetSession() #saves 10 seconds when gateway is run again
      return bot.gateway.session.guild(guild_id).members

  members = get_members('guild id here', 'channel id here')
  memberslist = []
  with open("ids.json", "r") as file:
    data = json.load(file)
  total_scraped = 0
  for memberID in members:
    if memberID not in data:
      total_scraped += 1
      data.append(int(memberID))
      print(f"{total_scraped}/{len(members)} - {memberID}")
  with open("ids.json", "w") as file:
    json.dump(data, file)
  end = time.time()
  print(f"Scraped {total_scraped} User IDs successfully\nTime Taken: {end - start}s")

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
  [2] Id Scraper
  [3] Coming soon.

  [4] Go back
    
    """)
    USER_OPT = input("Option\n> ")
    if USER_OPT == "1":
      clearcmd()
      massdm()
    elif USER_OPT == "2":
      underdev()
      back()
      clearcmd()
      self_bot()
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
  [3] Nitro Gift Generator
  [4] Nitro Gift Checker (Not Stable)
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
