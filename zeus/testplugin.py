from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon import TelegramClient, events, sync


@events.register(events.NewMessage(pattern=".ascii"))
async def ascii(event):
    if not event.reply_to_msg_id:
        return await event.edit("Reply to any user message.😒🤐")
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        return await event.edit("Reply to media message😒🤐")
    bot = "@asciiart_bot"
    #cid = await client_id(event)
 #   hell_mention = cid[2]
    kraken = await event.edit("Wait making ASCII...🤓🔥🔥")
    async with event.client.conversation(bot) as conv:
        try:
            first = await conv.send_message("/start")
            response = await conv.get_response()
            second = await conv.send_message(reply_message)
            output_op = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await parse_error(event, "Unblock @asciiart_bot and try again.", False)
            return
    await event.client.send_file(
        event.chat_id,
        file=output_op,
        caption=f"ASCII art By ",
        force_document=False,
    )
    await kraken.delete()
    await event.client.delete_messages(
        conv.chat_id, [first.id, response.id, second.id, output_op.id]
    )
