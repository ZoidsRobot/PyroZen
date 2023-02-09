from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as zen
from pyrogram.errors import MessageNotModified
from PyroZen.helpers.basic import *
from PyroZen.helpers.adminHelpers import DEVS
from config import *
from config import CMD_HANDLER as cmd
from PyroZen.utils import *

import requests
import os
import json
import random

@zen.on_message(filters.command("cask", cmd) & filters.user(DEVS) & ~filters.me)
@zen.on_message(filters.command("ask", cmd) & filters.me)
async def openai(client: Client, message: Message):
    if len(message.command) == 1:
        return await message.reply(f"Ketik <code>.{message.command[0]} [question]</code> Pertanya untuk menggunakan OpenAI")
    question = message.text.split(" ", maxsplit=1)[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }

    json_data = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 200,
        "temperature": 0,
    }
    msg = await message.reply("`Sabar..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception:
        await msg.edit("Terjadi Kesalahan!!\nAnda Belum Memasukan OPENAI_API_KEY")
        
 add_command_help(
    "google",
    [
        [
            f"google atau {cmd}ask",
            "Untuk Bertanya Pada Bot",
        ]
    ],
)

