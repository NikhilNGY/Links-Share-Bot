# +++ Modified By Yato [telegram username: @i_killed_my_clan & @ProYato] +++ # aNDI BANDI SANDI JISNE BHI CREDIT HATAYA USKI BANDI RAndi 
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "2468192"))
API_HASH = os.environ.get("API_HASH", "4906b3f8f198ec0e24edb2c197677678")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", "2068233407"))
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "Filter2")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nYᴏᴜʀ Rᴇǫᴜᴇsᴛ Tᴏ Jᴏɪɴ {title} Is Aᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @KR_Picture</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

# Start pic
START_PIC_FILE_ID = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
START_IMG = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
# Messages
START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote>Fʀɪᴇɴᴅꜱ.......🖤\n  Wᴇ Hᴀᴠᴇ Aʟʀᴇᴀᴅʏ Lᴏꜱᴛ Mᴀɴʏ Cʜᴀɴɴᴇʟꜱ Dᴜᴇ Tᴏ Cᴏᴘʏʀɪɢʜᴛ... Sᴏ Jᴏɪɴ Uꜱ Bʏ Gɪᴠɪɴɢ Yᴏᴜʀ Sᴜᴘᴘᴏʀᴛ, Cᴏᴏᴘᴇʀᴀᴛɪᴏɴ Aɴᴅ Bʟᴇꜱꜱɪɴɢꜱ Tᴏ Tʜɪꜱ Nᴇᴡ Cʜᴀɴɴᴇʟ Oꜰ Oᴜʀꜱ 🙏🙏 Tᴇᴀᴍ: @KR_Picture</blockquote></b>")
HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote>Aɴʏ Iꜱꜱᴜᴇꜱ Mᴏᴠɪᴇ Fɪʟᴇꜱ Cᴏɴᴛᴀᴄᴛ Oᴡɴᴇʀ\n      \n🍁 Oᴡɴᴇʀ: <a href=https://t.me/Nikhil5757h>Ｄ Ｉ Ｃ Ｔ Ａ Ｔ Ｏ Ｒ</a></blockquote></b>")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote>Aɴʏ Iꜱꜱᴜᴇꜱ Mᴏᴠɪᴇ Fɪʟᴇꜱ Cᴏɴᴛᴀᴄᴛ Oᴡɴᴇʀ\n      \n🍁 Oᴡɴᴇʀ: <a href=https://t.me/Nikhil5757h>Ｄ Ｉ Ｃ Ｔ Ａ Ｔ Ｏ Ｒ</a></blockquote></b>")

ABOUT_TXT = """<b><blockquote>Aɴʏ Iꜱꜱᴜᴇꜱ Mᴏᴠɪᴇ Fɪʟᴇꜱ Cᴏɴᴛᴀᴄᴛ Oᴡɴᴇʀ\n      \n🍁 Oᴡɴᴇʀ: <a href=https://t.me/Nikhil5757h>Ｄ Ｉ Ｃ Ｔ Ａ Ｔ Ｏ Ｒ</a></blockquote></b>"""

CHANNELS_TXT = """<b><blockquote>Aɴʏ Iꜱꜱᴜᴇꜱ Mᴏᴠɪᴇ Fɪʟᴇꜱ Cᴏɴᴛᴀᴄᴛ Oᴡɴᴇʀ\n      \n🍁 Oᴡɴᴇʀ: <a href=https://t.me/Nikhil5757h>Ｄ Ｉ Ｃ Ｔ Ａ ＴＯ Ｒ</a></blockquote></b>"""

#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b><blockquote>❌ Dᴏɴ'ᴛ Sᴇɴᴅ Mᴇ Mᴇꜱꜱᴀɢᴇꜱ, Sᴇɴᴅ Mᴇꜱꜱᴀɢᴇ Iɴ Gʀᴏᴜᴘ Oɴʟʏ Tᴇᴀᴍ : @KR_Picture</blockquote></b>"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1001693006436")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "2068233407").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(2068233407)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
