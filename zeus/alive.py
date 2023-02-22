from telethon import TelegramClient, events
import zeus.client
import os
import time
client = zeus.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.alive'))
async def alive(noob_py):
		client = noob_py.client
		me = await client.get_me()
		username = me.username
		darknet7719 = await client.download_profile_photo(username)
		await client.edit_message(noob_py.message, "Hayrli kun...")
		time.sleep(0.5)
		await noob_py.respond("""🥷 **Foydalanuvchi**: @{}

🥷 **Versia**: 1.0.1.3
├╴╴╴╴╴╴╴╴╴╴
└ 🧟‍♀️ **gojo Userbot**: @gojo_ub

 👾 **2021yil 10oy 19kun dasturlangan**
 👾 **ajdodi**: magicbot-uz
 👾 **Dasturchi**: @master_darknet

🥷 OʻRNATISH 
├╴╴╴╴╴╴╴╴╴╴
├ 👾 https://t.me/gojo_ub
└ 👾 https://t.me/darknet_off1cial,""".format(username, ' '), file=darknet7719)
		await noob_py.message.delete()
		os.remove(darknet7719)