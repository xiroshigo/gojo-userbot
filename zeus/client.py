from telethon import TelegramClient, sync
from telethon.sessions import StringSession
import getpass
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from time import sleep
import os, sys
api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
os.system('clear')
print("""\033[31m
▒█▀▀█ 
▒█░▄▄
▒█▄▄█ 
""")
sleep(0.5)
os.system("clear")
print("""

▒█▀▀█ ▒█▀▀▀█ 
▒█░▄▄ ▒█░░▒█ 
▒█▄▄█ ▒█▄▄▄█ 
""")
sleep(0.5)
os.system("clear")
print("""

▒█▀▀█ ▒█▀▀▀█ ░░░▒█ 
▒█░▄▄ ▒█░░▒█ ░▄░▒█ 
▒█▄▄█ ▒█▄▄▄█ ▒█▄▄█ 
""")
sleep(0.5)
os.system("clear")
print("""

▒█▀▀█ ▒█▀▀▀█ ░░░▒█ ▒█▀▀▀█ 
▒█░▄▄ ▒█░░▒█ ░▄░▒█ ▒█░░▒█ 
▒█▄▄█ ▒█▄▄▄█ ▒█▄▄█ ▒█▄▄▄█
""")

string = input("session code: ")

with TelegramClient(StringSession(string), api_id, api_hash) as client:
    #print(client.session.save())
    client.send_message("me", client.session.save())


 
 
  	
	#modules

	    

  