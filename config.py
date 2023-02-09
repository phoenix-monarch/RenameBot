import os
import re

id_pattern = re.compile(r'^.\d+$')
# get a token from @BotFather
TOKEN = os.environ.get("TOKEN", "5856240606:AAEjcLABjVHkJMRdDZvX0I7ev3rDiS0rwrM")
# The Telegram API things
APP_ID = int(os.environ.get("APP_ID", "23890262"))
API_HASH = os.environ.get("API_HASH", "da7e86cf57b0e6220b8a9e0aed228a68")
#Array to store users who are authorized to use the bot
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
#Your Mongo DB Database Name
DB_NAME = os.environ.get("DB_NAME", "tgpsychobotz")
#Your Mongo DB URL Obtained From mongodb.com
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Miyuki:MiyukiX@cluster0.egad6tb.mongodb.net/?retryWrites=true&w=majority")

START_PIC = (os.environ.get("START_PIC", "https://telegra.ph/file/81169a0f4e465f412bf67.jpg")).split()

PORT = os.environ.get("PORT", "8080")

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001572271892")

FLOOD = int(os.environ.get("FLOOD", "5"))
