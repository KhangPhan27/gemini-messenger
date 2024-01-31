from os import environ
from os.path import join, dirname
from dotenv import load_dotenv
from fbapy import *
from gemini import gemini
from threading import Thread
load_dotenv(join(dirname(__file__), ".env"))
client = Client()
api = client.login(
    appstate=environ.get("APPSTATE"),
    options={
        "user_agent": "Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"
    },
)
()
def callback(events, api: API):
    if events["type"]=="message":
        Thread(target=lambda:
               api.send_message(
                   text=gemini(events["body"]),
                   thread_id=events["thread_id"],
                   message_id=events["message_id"]
                                )).start()
        
api.listen_mqtt(callback)