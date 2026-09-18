# AI Voice Assistant

A Python desktop voice assistant with a PyQt interface, speech recognition, text-to-speech through Chrome, simple command handling, and Gemini-powered replies.

## Project highlights

- Built a desktop interface with PyQt5 for starting and monitoring the assistant.
- Integrated microphone input, language translation, browser-based text-to-speech, and desktop/web command handling.
- Added Gemini-powered conversational responses alongside a lightweight PyTorch intent classifier.
- Uses environment-based configuration so API credentials stay out of source control.

## Before you start

This project needs a Gemini API key. Never paste that key into source code or commit a `.env` file.

1. Copy `.env.example` to a new file named `.env`.
2. Put your own key after `GEMINI_API_KEY=`.
3. Install the required packages:

   ```bash
   python -m pip install -r requirements.txt
   python -m nltk.downloader punkt
   ```

4. Start the assistant:

   ```bash
   python jarvis.py
   ```

## Notes

- The first run trains the small command model and stores it locally in `Database/Tasks.pth`.
- A Chrome installation is required for the current text-to-speech implementation.
- `Database/` contains local chat history and is intentionally excluded from Git.

## Security

If an API key was previously committed or shared, revoke it in its provider dashboard and create a replacement before use.
