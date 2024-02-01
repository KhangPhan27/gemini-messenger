import requests, json
from os import environ
from dotenv import load_dotenv
from os.path import join, dirname
# config Gemini model
load_dotenv(join(dirname(__file__), ".env"))
api_key=environ.get("GEMINI_API")


def gemini(message):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": message
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    try:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "Đã có lỗi xảy ra!"
