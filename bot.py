import logging
import logging.config
from pyrogram import Client
import os

from config import Config

from aiohttp import web
from plugins.web import web_server
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

FORCE_SUB = os.environ.get("FORCE_SUB", "")
PORT = os.environ.get("PORT", "8080")

    if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            bot_token=Config.TOKEN,
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            workers=50,
            plugins=plugins,
            sleep_threshold=5,
        )

    async def start(self):
       await super().start()
       me = await self.get_me()
       self.mention = me.mention
       self.username = me.username 
       self.force_channel = FORCE_SUB
       if FORCE_SUB:
         try:
            link = await self.export_chat_invite_link(FORCE_SUB)                  
            self.invitelink = link
         except Exception as e:
            logging.warning(e)
            logging.warning("Make Sure Bot admin in force sub channel")             
            self.force_channel = None
       app = web.AppRunner(await web_server())
       await app.setup()
       bind_address = "0.0.0.0"
       await web.TCPSite(app, bind_address, PORT).start()
       logging.info(f"{me.first_name} Started 👿👿👿")
      

    async def stop(self, *args):
      await super().stop()      
      logging.info("Bot Stopped")
        
app = Bot()
app.run()
