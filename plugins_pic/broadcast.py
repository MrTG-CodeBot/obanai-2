from pyrogram import Client, filters
import datetime
import time
from database_pic.pic_users_db import sd
from info import ADMINS
from utils import broadcast_messager
import asyncio

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
async def broadcast(bot, message):
 try:
    users = await sd.get_all_users()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ...'
    )
    start_time = time.time()
    total_users = await sd.total_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed =0

    success = 0
    async for user in users:
        pti, sh = await broadcast_messager(int(user['id']), b_msg)
        if pti:
            success += 1
        elif pti == False:
            if sh == "Blocked":
                blocked+=1
            elif sh == "Deleted":
                deleted += 1
            elif sh == "Error":
                failed += 1
        done += 1
        await asyncio.sleep(2)
        if not done % 20:
            await sts.edit(f"ʙʀᴏᴀᴅᴄᴀsᴛ ɪɴ ᴘʀᴏɢʀᴇss:\n\nᴛᴏᴛᴀʟ ᴜsᴇʀs {total_users}\nᴄᴏᴍᴘʟᴇᴛᴇᴅ: {done} / {total_users}\nsᴜᴄᴇss: {success}\nʙʟᴏᴄᴋᴇᴅ: {blocked}\nᴅᴇʟᴇᴛᴇᴅ: {deleted}")    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍʟᴇᴛᴇᴅ:\nᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ {time_taken} sᴇᴄᴏɴᴅs.\n\nᴛᴏᴛᴀʟ ᴜsᴇʀ {total_users}\nᴄᴏᴍᴘʟᴇᴛᴇᴅ: {done} / {total_users}\nsᴜᴄᴇss: {success}\nʙʟᴏᴄᴋᴇᴅ: {blocked}\nᴅᴇʟᴇᴛᴇᴅ: {deleted}")
 except Exception as e:
    await message.reply_text(e)
