# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27039000"))
API_HASH = getenv("API_HASH", "5397095439b5ae9d00634ed2e98ff3e0")
BOT_TOKEN = getenv("BOT_TOKEN", "8036891972:AAF_IctBoFsBsR9V6uhYcbtZpeik3QVKABE")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7312764081").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://sachinkumar0989770:<db_KgY6lo10lz3H4xs6>@cluster0.klz8w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002484813187")
CHANNEL_ID = int(getenv("CHANNEL_ID", "1002300843475"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
