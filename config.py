import os
import re

id_pattern = re.compile(r'^.\d+$')
# get a token from @BotFather
TOKEN = os.environ.get("TOKEN", "")
# The Telegram API things
APP_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
#Array to store users who are authorized to use the bot
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
#Your Mongo DB Database Name
DB_NAME = os.environ.get("DB_NAME", "my")
#Your Mongo DB URL Obtained From mongodb.com
DB_URL = os.environ.get("DB_URL", "")

START_PIC = (os.environ.get("START_PIC", "https://telegra.ph/file/0e3738d56ff92e363a1d9.jpg https://telegra.ph/file/a52e97c3371d6197e7723.jpg https://telegra.ph/file/da8e1ab9f84ba60494451.jpg https://telegra.ph/file/cfa28e7e2fe19adc9688c.jpg https://telegra.ph/file/be339f05202e87a05515c.jpg https://telegra.ph/file/45c1e617e959edc7f3aee.jpg https://telegra.ph/file/f0e48c64e7ee4ee304407.jpg https://telegra.ph/file/ac16ec543b2fb84be97d2.jpg https://telegra.ph/file/4f1303bf89fd84843f172.jpg")).split()

PORT = os.environ.get("PORT", "8080")

FORCE_SUB = os.environ.get("FORCE_SUB", "")

FLOOD = int(os.environ.get("FLOOD", "5"))
