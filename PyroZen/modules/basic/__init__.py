import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "PyroZen"])

async def join(client):
    try:
        await client.join_chat("ZennXSupport")
        await client.join_chat("zennihhh")
        await client.join_chat("StoryMan01")
    except BaseException:
        pass
