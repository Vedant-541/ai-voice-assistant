#using gemini for chatbot
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("Set GEMINI_API_KEY in a local .env file before starting Jarvis.")
genai.configure(api_key=api_key)

def QuestionAnswer(question,chat_log = None):
    FileLog = open("Database/qna_log.txt","r")#where chat will be saved
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
    FileLog = open("Database/qna_log.txt","w")
    FileLog.write(chat_log_template_update)#saving response
    FileLog.close()
    return answer
