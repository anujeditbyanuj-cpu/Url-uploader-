# © aceknox

import logging
import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import os
from config import Config
from translation import Translation
from pyrogram import filters
from database.adduser import AddUser
from pyrogram import Client as Clinton
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Random Start Photos

PICS = (
    "https://img3.teletype.in/files/67/73/67735f4f-933a-41d9-86b9-609fa03b6614.jpeg",
    "https://img3.teletype.in/files/a6/b6/a6b666ef-afa0-4793-bd6b-235265258840.jpeg",
    "https://img3.teletype.in/files/e8/01/e8013193-9299-4cdc-8222-f4e3801a05e8.jpeg",
    "https://img4.teletype.in/files/77/7f/777f2c2d-fa53-4298-9dee-ab39d9bddf81.jpeg",
    "https://img3.teletype.in/files/a1/9e/a19e9352-dfee-471a-ae3f-14eb2e1b975b.jpeg",
    "https://img1.teletype.in/files/84/84/8484934a-a247-4b1a-8f1f-74aac621bea6.jpeg",
    "https://img4.teletype.in/files/b2/89/b289d67c-2299-4cf6-91c3-b84c83c57caa.jpeg",
    "https://img3.teletype.in/files/a0/49/a049a7b1-2924-41c1-95d4-8c466c1a80ad.jpeg",
    "https://img2.teletype.in/files/59/b3/59b3a62e-e2ce-4f00-847d-9910f0498884.jpeg",
    "https://img2.teletype.in/files/91/d8/91d8838b-85ec-45ff-868f-24d66126ce55.jpeg",

    # Anime Wallpapers
    "https://ik.imagekit.io/jbxs2z512/naruto_GxcPgSeOy.jpg?updatedAt=1748486799631",
    "https://ik.imagekit.io/jbxs2z512/hd-anime-prr1y1k5gqxfcgpv.jpg?updatedAt=1748487947183",
    "https://ik.imagekit.io/jbxs2z512/dazai-osamu-sunset-rooftop-anime-wallpaper-cover.jpg?updatedAt=1748488276069",
    "https://ik.imagekit.io/jbxs2z512/thumb-1920-736461.png?updatedAt=1748488419323",
    "https://ik.imagekit.io/jbxs2z512/116847-3840x2160-desktop-4k-bleach-background-photo.jpg?updatedAt=1748488510841",
    "https://ik.imagekit.io/jbxs2z512/thumb-1920-1361035.jpeg?updatedAt=1748488911202",
    "https://ik.imagekit.io/jbxs2z512/thumb-1920-777955.jpg?updatedAt=1748488978230",
    "https://ik.imagekit.io/jbxs2z512/akali-wallpaper-960x540_43.jpg?updatedAt=1748489275125",
    "https://ik.imagekit.io/jbxs2z512/robin-honkai-star-rail-497@1@o?updatedAt=1748490140360",

    # More Wallpapers
    "https://ik.imagekit.io/jbxs2z512/wp14288215.jpg?updatedAt=1748492348766",
    "https://ik.imagekit.io/jbxs2z512/8k-anime-girl-and-flowers-t4bj6u55nmgfdrhe.jpg?updatedAt=1748493169919",
    "https://ik.imagekit.io/jbxs2z512/attack-on-titan-mikasa-cover-image-ybt96t1e1041qdt3.jpg?updatedAt=1748493720903",
    "https://ik.imagekit.io/jbxs2z512/tsunade-at-her-desk-bakoh4jeg42sjn3c.jpg?updatedAt=1748493962363",
    "https://ik.imagekit.io/jbxs2z512/Fight-Break-Sphere.png?updatedAt=1750042299023",
    "https://ik.imagekit.io/jbxs2z512/shanks-divine-departure-attack-in-one-piece-sn.jpg?updatedAt=1750043121252",

    # Ultra HD
    "https://ik.imagekit.io/jbxs2z512/thumbbig-1345576.webp?updatedAt=1751108065802",
    "https://ik.imagekit.io/jbxs2z512/thumbbig-1335194.webp?updatedAt=1751108710765",
    "https://ik.imagekit.io/jbxs2z512/thumbbig-1373976.webp?updatedAt=1751108748746",
    "https://ik.imagekit.io/jbxs2z512/thumbbig-1065277.webp?updatedAt=1751108877871",
    "https://ik.imagekit.io/jbxs2z512/thumbbig-877141.webp?updatedAt=1751108916209",

    # New Collection
    "https://ik.imagekit.io/jbxs2z512/876145-3840x2160-desktop-4k-konan-naruto-background-image%20(1).jpg?updatedAt=1751109523353",
    "https://ik.imagekit.io/jbxs2z512/tumblr_9663cff78634f174f81b41b64fc450df_66ebd999_1280%20(1).png?updatedAt=1751109523759",
    "https://ik.imagekit.io/jbxs2z512/anime-girl-demon-horn-art-4k-wallpaper-uhdpaper.com-714@2@b%20(1).jpg?updatedAt=1751109524369",
    "https://ik.imagekit.io/jbxs2z512/dbbb586df338d55d340ec650bcdd74fe.jpg?updatedAt=1751110984735",
    "https://ik.imagekit.io/jbxs2z512/c02aecb70c3c6a5b1f51ba09e4d2cc70.jpg?updatedAt=1751111979586",
    "https://ik.imagekit.io/jbxs2z512/6c2618a1eea58d22e2d1a5ba99c95a1c.jpg?updatedAt=1751112051082",
    "https://ik.imagekit.io/jbxs2z512/7a82750e26bf451ab1775993279e2c64.jpg?updatedAt=1751112189297",
)

@Clinton.on_message(filters.private & filters.command(["files"]))
async def test(bot, message):
    if message.from_user.id != Config.OWNER_ID:
        return
    if len(message.text.split(" ")) == 2:
        user_id = message.text.split(" ")[1]
        if user_id == "me":
            user_id == Config.OWNER_ID
        path = Config.DOWNLOAD_LOCATION + str(user_id) + "/"
        try:
            files = os.listdir(path)
            joined_files = "\n".join(files)
            await message.reply_text(
                str(joined_files),
                quote=True
            )
        except:
            await message.reply_text(
                "No files found.",
                quote=True
            )
            return
    else:
        path = Config.DOWNLOAD_LOCATION
        try:
            files = os.listdir(path)
            joined_files = "\n".join(files)
            await message.reply_text(
                str(joined_files),
                quote=True
            )
        except:
            await message.reply_text(
                "No files found.",
                quote=True
            )
            return

@Clinton.on_message(filters.private & filters.reply & filters.text)
async def edit_caption(bot, update):
    try:
        await bot.send_cached_media(
            chat_id=update.chat.id,
            file_id=update.reply_to_message.video.file_id,
            reply_to_message_id=update.message_id,
            caption=update.text
        )
    except:
        try:
            await bot.send_cached_media(
                chat_id=update.chat.id,
                file_id=update.reply_to_message.audio.file_id,
                reply_to_message_id=update.message_id,
                caption=update.text
            )
        except:
            try:
                await bot.send_cached_media(
                    chat_id=update.chat.id,
                    file_id=update.reply_to_message.document.file_id,
                    reply_to_message_id=update.message_id,
                    caption=update.text
                )
            except:
                pass

@Clinton.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    await AddUser(bot, update)
    await update.reply_text(
        Translation.HELP_USER,
        quote=True
    )

@Clinton.on_message(filters.private & filters.command(["addcaption"]))
async def add_caption_help(bot, update):
    await AddUser(bot, update)
    await update.reply_text(
        Translation.ADD_CAPTION_HELP,
        quote=True
    )

@Clinton.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):

    await AddUser(bot, update)

    photo = random.choice(PICS)

    await bot.send_photo(
        chat_id=update.chat.id,
        photo=photo,
        caption=Translation.START_TEXT.format(update.from_user.first_name),
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(
            [

                [
                    InlineKeyboardButton(
                        "Channel ⚡",
                        url="https://t.me/url_anuj_bot"
                    ),

                    InlineKeyboardButton(
                        "Developer 👨‍⚖️",
                        url="https://t.me/anujedits76"
                    ),

                ],

            ]
        ),
        reply_to_message_id=update.message_id
    )
