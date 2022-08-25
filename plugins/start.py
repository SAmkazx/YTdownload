
from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Updates Channel", url="https://t.me/Latest_hindi_hd_Movies_Hub")
      ],
      [ 
        InlineKeyboardButton(
            "Support Group", url="https://t.me/Latest_hindi_hd_Movies_Hub")]
    ])
    welcomed = f"<b> Hey {message.from_user.first_name} , \n\nI'm YouTube DL 📥📥 Bot. I can 📥📥 download video or audio f\n from Youtube. \n\nMade by @DeltaBotsOfficial /n/n /help for More info </b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagatio
