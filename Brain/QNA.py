
    return answer
# Gemini-powered question answering
import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("Set GEMINI_API_KEY in a local .env file before starting the voice assistant.")
genai.configure(api_key=api_key)


def QuestionAnswer(question, chat_log=None):
    with open("Database/qna_log.txt", "r") as file_log:
        chat_log_template = file_log.read()

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
    answer = model.start_chat().send_message(question).text
    chat_log_template_update = chat_log_template + f"\nYou: {question}\nAssistant: {answer}"
    with open("Database/qna_log.txt", "w") as file_log:
        file_log.write(chat_log_template_update)
    return answer
