#using gemini for chatbot
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("Set GEMINI_API_KEY in a local .env file before starting Jarvis.")
genai.configure(api_key=api_key)

def ReplyBrain(question,chat_log = None):
    FileLog = open("Database/chat_log.txt","r")#where chat will be saved
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt =f'{chat_log}You : {question}\nJarvis : '
    #gemini model cofiguration
    generation_config = {
     "temperature": 1,
     "top_p": 0.95,
     "top_k": 40,
     "max_output_tokens": 8192,
     "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
     model_name="gemini-1.5-pro-002",
     generation_config=generation_config,
    )

    response = model.start_chat().send_message(question)
    answer=response.text# response of question
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nJarvis : {answer}"
    FileLog = open("Database/chat_log.txt","w")
    FileLog.write(chat_log_template_update)#saving response
    FileLog.close()
    return answer


'''
import openai
from dotenv import load_dotenv

openai.api_key = ""
load_dotenv()
completion = openai.completions

def ReplyBrain(question,chat_log = None):
    FileLog = open("Database/chat_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt =f'{chat_log}You : {question}\nJarvis : '
    response = completion.create(
        model = "gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.5,
        max_tokens =60,
        top_p =0.3,
        frequency_penalty =0.5,
        presence_penalty =0)
    answer =response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nJarvis : {answer}"
    FileLog = open("Database/chat_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer
ReplyBrain("Hello")
'''
