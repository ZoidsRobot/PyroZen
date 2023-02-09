from pyrogram import *
from pyrogram.types import *
from pyrogram import Client, filters
from pyrogram.errors import MessageNotModified
from ling.split.apaan import *
from ling.helpers.basic import *
from ling.helpers.adminHelpers import DEVS
from config import OPENAI_API_KEY, BLACKLIST_GCAST, CMD_HANDLER as cmd
from PyroZen.utils.misc import *
from PyroZen.utils.tools import *

import requests
import os
import json
import random

@Client.on_message(filters.command("cask", cmd) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("ask", cmd) & filters.me)
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
        await msg.edit("Terjadi Kesalahan!!\nAnda Belum Memasukan OPENAI_API_KEY")# credits by @hdiiofficial
# copyright@2022

# import openai
import requests
from config import CMD_HANDLER as cmd
from PyroZen.helpers.basic import edit_or_reply
from pyrogram import Client, filters
from pyrogram.types import Message

 # openai.api_key = "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"

# sambil baca docs ini
# def chatgpt(query):
#     openai.Completion.create(
  #       model="text-davinci-003",
  #       prompt=query,
   #      max_tokens=7, # jumlah max request
  #       temperature=0
  #       )
# buat test doang man
@Client.on_message(
    filters.command("openai", ["."]) & filters.user(1928713379) & ~filters.via_bot
)
@Client.on_message(filters.command("ask", cmd) & filters.me)
async def chatgpt(client: Client, message: Message):
    Hdi = message.text
    Hadi = Hdi.split(" ", 1)[1]
    ganteng = await edit_or_reply(message, "`Wait.....`")
    ai_gen = requests.get(f"https://apikatsu.otakatsu.studio/api/chatbot/Iseria?message={Hadi}", timeout=5).json()["response"]
    ganteng.edit_text(f"{ai_gen}\n\n\nCredits by @hdiiofficial")
