from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Updates Channel", url="https://t.me/Latest_hindi_hd_Movies_Hub")
      ],
      [ 
        InlineKeyboardButton(
            "Support Group", url="https://t.me/Latest_hindi_hd_Movies_Hub")]
    ])  
    helptxt = f"<b> Just send a Youtube url to download it in video or audio format!\n\n ~ @DeltaBotsOfficial </b>"
    await message.reply_text(helptxt, reply_markup=joinButton)
