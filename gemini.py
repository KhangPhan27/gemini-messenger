import google.generativeai as genai
from os import environ
from dotenv import load_dotenv
from os.path import join, dirname
# config Gemini model
load_dotenv(join(dirname(__file__), ".env"))
genai.configure(api_key=environ.get("GEMINI_API"))
model = genai.GenerativeModel('gemini-pro')

def gemini(content:str):
    response = model.generate_content(contents=content)
    return response.text



    
