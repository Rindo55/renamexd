from pyrogram import Client
from config import *
from route import web_server
from aiohttp import web

    async def start(self):  
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        port = "8080"
        await web.TCPSite(app, bind_address, port).start()   
        print(f"{"hello"} | bot 𝚂𝚃𝙰𝚁𝚃𝙴𝙳...⚡️")
       


bot = Bot()
bot.run()
