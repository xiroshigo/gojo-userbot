from telethon import TelegramClient, events, sync, functions, types, Button

import zeus.client
client = zeus.client.client
botClient = zeus.client.botClient
@botClient.on(events.InlineQuery)
async def _(query):
				if query.text == "ppphelp":
								result = query.builder.article('ppphelp', text = """
GOJO USERBOT HELP MENU 					
								""", buttons= [
								[Button.inline("Bombs", data=b"1"), Button.inline("magic", data=b"2"), Button.inline("loading",data=b"3")],
								
								[Button.inline("Dump", data=b"4"), Button.inline("18+", data=b"5"), Button.inline("LUL",data=b"6")],
								
								[Button.inline("Snake", data=b"7"), Button.inline("NotHappy", data=b"8"), Button.inline("Muah",data=b"9")],
								
								[Button.inline("Tmoon", data=b"10"), Button.inline("Smoon", data=b"11"), Button.inline("moon",data=b"12")],
								
								[Button.inline("Clock", data=b"13"), Button.inline("Candy", data=b"14"), Button.inline("Heart",data=b"15")],
								
								[Button.inline("Gymnastic", data=b"16"), Button.inline("clown", data=b"17"), Button.inline("Star",data=b"18")],
								
								[Button.inline("Earth", data=b"19"), Button.inline("Snow", data=b"20"), Button.inline("Rain",data=b"21")],
								
								[Button.inline("Clol", data=b"22"), Button.inline("Jio", data=b"23"), Button.inline("Police",data=b"24")]])
								
								await query.answer([result])
								
				
								
@botClient.on(events.CallbackQuery)
async def uzgaruvchi(event):
				
				if event.data==b'1':
					await event.answer("Animatsia bombs \nplugin: .bombs", alert=True)
					
				if event.data==b'2':
					await event.answer("Animatsia Heart emojies \nplugin: .magic", alert=True)
					
				if event.data==b'3':
					await event.answer("Animatsia loading \nplugin: .loading", alert=True)
					
				if event.data==b'4':
					await event.answer("Animatsia dump \nplugin: .dump", alert=True)
					
				if event.data==b'5':
					await event.answer("18+ animation\nplugin: .sexy", alert=True)
					
				if event.data==b'6':
					await event.answer("Animatsia lul \nplugin: .lul", alert=True)
				
				if event.data==b'7':
					await event.answer("Animatsua Snake\nPlugin: .snake", alert=True)
					
				if event.data==b'8':
					await event.answer("Animatsia NotHappy\nplugin: .nothappy", alert=True)
				
				if event.data==b'9':
					await event.answer("Animatsia Muah\nPlugin: .muah", alert=True)
				
				if event.data==b'10':
					await event.answer("Animatsia Tmoon\nPlugin: .tmoon", alert=True)
				
				if event.data==b'11':
					await event.answer("Animatsia Smoon\nPlugin: .smoon", alert=True)
				
				if event.data==b'12':
					await event.answer("Animatsia moon\nplugin: .moon", alert=True)
				
				if event.data==b'13':
					await event.answer("Animatsia Clock\nplugin: .clock", alert=True)
					
				if event.data==b'14':
					await event.answer("Animatsia Candy\nplugin: .candy", alert=True)
					
				if event.data==b'15':
					await event.answer("Animatsia Heart\nplugin: .heart", alert=True)
				
				if event.data==b'16':
					await event.answer("Animatsia Gymnastik\nplugin: .gym", alert=True)
				
				if event.data==b'17':
					await event.answer("Animatsia Clown\nplugin: .clown", alert=True)
				
				if event.data==b'18':
					await event.answer("Animatsia Star\nplugin: .star", alert=True)
				
				if event.data==b'19':
					await event.answer("Animatsia Earth\nPlugin: .earth", alert=True)
				
				if event.data==b'20':
					await event.answer("Animatsia Snow\nplugin: .snow", alert=True)
					
				if event.data==b'21':
					await event.answer("Animatsia Rain\nplugin: .rain", alert=True)
					
				if event.data==b'22':
					await event.answer("Animatsia clol\nplugin: .clol", alert=True)
					
				if event.data==b'23':
					await event.answer("Animatsia jio\nplugin: .jio", alert=True)
				
				if event.data==b'24':
					await event.answer("Animatsia police\nplugin:, .police", alert=True)
					
				

				
								
								
								
								

@events.register(events.NewMessage(pattern=".help", outgoing=True))
async def help(event):
				results = await client.inline_query("@gojo_userbot", "ppphelp")
			#	menu2 = await client.inline_query("@gojo_userbot", "pppphelp")
				await results[0].click(event.chat_id)

				await event.message.delete()
