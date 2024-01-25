import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6970285411:AAHHw0mq4Yowuv7U2sgxfmUsCrV3kERNJsc")

API_ID = int(os.environ.get("API_ID", "28647200"))

API_HASH = os.environ.get("API_HASH", "42e71744fb1829f43010bd6003224daf")

STRING = os.environ.get("STRING", "BQG1HyAAJyskqcGO3R0Uqrz-UTpYZ_f9lCcSJBtBJDk-Pnk9OMmgmjTIfPifIHn5VPeJZ1kNFsgeTmaFheJVihOjt7pvlQMxjEE2FdgpJbi_E9XiWZou1ugGwO0l_CRlKJ2FDQQjmmMV9WkvWDxubUhWhXnzWeabuuN9kfMJ9ix7nL3xkHkP98UircuPFK0c4Tw2whruv6C6uA_NofxK7vpC0iIdg70QZvDfARQ70mmR2xmc-34VQG8Umm3zGzy6zTYEqMmN6B2D00h2zXaIMsEiADrE7xqskks-lbGSQSSiAPx5_xOGdV7YERr-zXqML83oKNm5hDvGagnAqa3e_nx-PIpfnwAAAAB2ODvWAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
