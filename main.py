from telethon import TelegramClient, events, sync
#
from time import gmtime, strftime
from emoji import emojize
import asyncio

###
from emoji import emojize
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.utils import get_input_location
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio, aiocron, datetime
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, User
#import pyfiglet
import zeus.client, zeus.test, zeus.bombs, zeus.helpp, zeus.loading, zeus.emoji, zeus.dump, zeus.sexy, zeus.type, zeus.magicrun, zeus.animation, zeus.animation2, zeus.chatinfo, zeus.mq, zeus.mute, zeus.nq, zeus.fuck, zeus.rev, zeus.tr, zeus.userinfo, zeus.base64, zeus.react, zeus.snow, zeus.ar, zeus.smsbomb, zeus.qrc, zeus.rename, zeus.iptrace, zeus.spam, zeus.alive, zeus.tagall, zeus.afk, zeus.timer
#
client = zeus.client.client

#
with client as darknet:
	darknet.add_event_handler(zeus.test.test) 
with client as darknet:
	darknet.add_event_handler(zeus.bombs.bombs)
with client as darknet:
	darknet.add_event_handler(zeus.helpp.help) 
with client as darknet:
	darknet.add_event_handler(zeus.loading.loading) 
with client as darknet:
	darknet.add_event_handler(zeus.emoji.itachi) 
with client as darknet:
	darknet.add_event_handler(zeus.dump.dump) 	
with client as darknet:
	darknet.add_event_handler(zeus.sexy.sexy) 
with client as darknet:
	darknet.add_event_handler(zeus.type.type) 
with client as darknet:
	darknet.add_event_handler(zeus.magicrun.magicrun) 	
with client as darknet:
	darknet.add_event_handler(zeus.animation.lul)
with client as darknet:
	darknet.add_event_handler(zeus.animation.snake)
with client as darknet:
	darknet.add_event_handler(zeus.animation.nothappy)
with client as darknet:
	darknet.add_event_handler(zeus.animation.clock)
with client as darknet:
	darknet.add_event_handler(zeus.animation.muah)
with client as darknet:
	darknet.add_event_handler(zeus.animation.heart)	
with client as darknet:
	darknet.add_event_handler(zeus.animation.gym)
with client as darknet:
	darknet.add_event_handler(zeus.animation.earth)
with client as darknet:
	darknet.add_event_handler(zeus.animation.moon)
with client as darknet:
	darknet.add_event_handler(zeus.animation.candy)
with client as darknet:
	darknet.add_event_handler(zeus.animation.smoon)
with client as darknet:
	darknet.add_event_handler(zeus.animation.tmoon)
with client as darknet:
	darknet.add_event_handler(zeus.animation.clown)
with client as darknet:
	darknet.add_event_handler(zeus.animation2.star)
with client as darknet:
	darknet.add_event_handler(zeus.animation2.boxs)		
with client as darknet:
	darknet.add_event_handler(zeus.animation2.rain)
with client as darknet:
	darknet.add_event_handler(zeus.animation2.clol)
with client as darknet:
	darknet.add_event_handler(zeus.animation2.odra)
with client as darknet:
	darknet.add_event_handler(zeus.animation2.fleaveme)		
with client as darknet:
	darknet.add_event_handler(zeus.animation2.loveu)
with client as darknet:
	darknet.add_event_handler(zeus.animation2.plane)
with client as darknet:
	darknet.add_event_handler(zeus.animation2.police)
with client as darknet:
	darknet.add_event_handler(zeus.animation2.jio)		
with client as darknet:
	darknet.add_event_handler(zeus.animation2.solarsystem)
with client as darknet:
	darknet.add_event_handler(zeus.chatinfo.info)
with client as darknet:
	darknet.add_event_handler(zeus.mq.mq)
with client as darknet:
	darknet.add_event_handler(zeus.mute.mute)		
with client as darknet:
	darknet.add_event_handler(zeus.nq.nq)	
with client as darknet:
	darknet.add_event_handler(zeus.fuck.fuck)					
with client as darknet:
	darknet.add_event_handler(zeus.rev.rev)										
with client as darknet:
	darknet.add_event_handler(zeus.tr.tr)
with client as darknet:
	darknet.add_event_handler(zeus.userinfo.userinfo)
with client as darknet:
	darknet.add_event_handler(zeus.base64.runb64)				
with client as darknet:
	darknet.add_event_handler(zeus.react.react)
with client as darknet:
	darknet.add_event_handler(zeus.snow.snow)
with client as darknet:
	darknet.add_event_handler(zeus.ar.runar)
with client as darknet:
	darknet.add_event_handler(zeus.qrc.runqrc)
with client as darknet:
	darknet.add_event_handler(zeus.rename.rename)	
with client as darknet:
	darknet.add_event_handler(zeus.iptrace.iptrace)
	#spam
with client as darknet:
	darknet.add_event_handler(zeus.spam.delayspam)
	#
with client as darknet:
	darknet.add_event_handler(zeus.smsbomb.runj)
	#alive	
with client as darknet:
	darknet.add_event_handler(zeus.alive.alive)
	#tagall
with client as darknet:
	darknet.add_event_handler(zeus.tagall.tagall)
	#afk
with client as darknet:
	darknet.add_event_handler(zeus.afk.runafkon)
with client as darknet:
	darknet.add_event_handler(zeus.afk.runafkoff)
with client as darknet:
	darknet.add_event_handler(zeus.afk.runafkstatus)
with client as darknet:
	darknet.add_event_handler(zeus.afk.runmcfafk)
with client as darknet:
	darknet.add_event_handler(zeus.afk.runafk)
with client as darknet:
	darknet.add_event_handler(zeus.timer.timer)
with client as darknet:
	darknet.add_event_handler(zeus.timer.numbers)
with client as darknet:
	darknet.add_event_handler(zeus.timer.clocku)
with client as darknet:
	darknet.add_event_handler(zeus.timer.runsda)
with client as darknet:
	darknet.add_event_handler(zeus.timer.runrda)
with client as darknet:
	darknet.add_event_handler(zeus.timer.rundrc)
with client as darknet:
	darknet.add_event_handler(zeus.timer.runrts)		
with client as darknet:
	darknet.add_event_handler(zeus.timer.runrgm)	
with client as darknet:
	darknet.add_event_handler(zeus.timer.aboutclock)

	
	
client.start()
  
#result = pyfiglet.figlet_format("G O J O", font = "alligator" )
print("started")

client.run_until_disconnected()
