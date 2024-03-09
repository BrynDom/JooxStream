from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("ChatGPT", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("Groups", callback_data="mplus HELP_Group"),InlineKeyboardButton("Stickers", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("Tag-All", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("Info", callback_data="mplus HELP_Info"),InlineKeyboardButton("Extra", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("Image", callback_data="mplus HELP_Image"),
    InlineKeyboardButton("Action", callback_data="mplus HELP_Action"),InlineKeyboardButton("Search", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("Fonts", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("Games", callback_data="mplus HELP_Game"),InlineKeyboardButton("T-Graph", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("Imposter", callback_data="mplus HELP_Imposter"),
    InlineKeyboardButton("Truth-Dare", callback_data="mplus HELP_TD"),InlineKeyboardButton("HasTag", callback_data="mplus HELP_HT")], 
    [InlineKeyboardButton("Tts", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("Fun", callback_data="mplus HELP_Fun"),InlineKeyboardButton("Quotly", callback_data="mplus HELP_Q")],
    [InlineKeyboardButton("SangMata", callback_data="mplus HELP_SangMata"),InlineKeyboardButton("Bot", callback_data="mplus HELP_Bot"),
    InlineKeyboardButton("Filters", callback_data="mplus HELP_Filters")],
    [InlineKeyboardButton("🎵 Musik", callback_data=f"settings_back_helper"), 
     InlineKeyboardButton("Back", callback_data=f"settingsback_helper"),]]
