import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

APP_ID = int(getenv("APP_ID", "18109107"))
API_HASH = getenv("API_HASH", "e6afc7383da3a10fa16a0a9675c3e037")
TG_BOT_TOKEN = getenv("TG_BOT_TOKEN", "5502331963:AAFxJ5vyAka0onxS-UnVFhN6-iO38-i8dUE")
TG_BOT_USERNAME = getenv("TG_BOT_USERNAME", "Botpqyubot")
STRING_SESSION = getenv("STRING_SESSION", "1ApWapzMBu05Zn-e0sj5yJD0hFLnYro5myrsph4QMipOY4xtGIDEQz58gT2HT4ZEG-89wPrgnoo8yhc_3YXT37_Dp-5anoOMBlArwJu_QJktbu-_mLeQPJnBGObHLdRXBI3QKPx4hmnwhx-HnV_n749QQMPgcUbTyRb8t2hBnTpjT1YhbsnUfikVknvdBCYL7Lsa1cv2BmPUAhNopP8ct5_XCFNTjD_EQML_q7rTmM8y_ZiFQ0ASP0MG7_fTr9ny6YSVNKGnOtmjAkz6TnBIimZyQaPohklfw2IPesYbcxMiX-mHp4UxWnL6wBLRruchvTAg-UGhVH67ICp2L3TBe0xRBPDDlgCU=")
COMMAND_HAND_LER = list(getenv("COMMAND_HAND_LER", ".").split())
ENV = getenv("ENV", "ANYTHING")

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid ••••••••••• 
DATABASE_URL = getenv("DATABASE_URL", "postgres://emaqlyfh:8El0bXqfSK80NW3pXoO_DvJVDCMmuin3@snuffleupagus.db.elephantsql.com/emaqlyfh")
