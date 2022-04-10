# import logging
import json

from pyrogram import Client

from data import whispers

plugins = dict(
    root="plugins",
    include=[
        "inline",
        "private"
    ]
)

# logging.basicConfig(level=logging.DEBUG)
print('==> MASTER ŞİRVAN')
Client("LegendGizli", plugins=plugins).run()
with open('data.json', 'w') as f:
    json.dump(whispers, f)
print('\n==> MASTER ŞİRVAN ')
