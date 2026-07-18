import os
import tempfile

import gradio as gr
import speech_recognition as sr
from gtts import gTTS
from google import genai

# ----------------------------------------
# Configure Gemini API
# ----------------------------------------

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "Please set the GEMINI_API_KEY environment variable."
    )

client = genai.Client(api_key=API_KEY)


# ----------------------------------------
# Speech to Text
# ----------------------------------------

def speech_to_text(audio_path):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)
        return text

    except sr.UnknownValueError:
        return "Sorry, I could not understand your voice."

    except Exception as e:
        return f"Speech Recognition Error: {str(e)}"


# ----------------------------------------
# Ask Gemini
# ----------------------------------------

def ask_gemini(text):
    if not text.strip():
        return "Please speak something."

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=text,
        )

        return response.text

    except Exception as e:
        return f"Gemini Error: {str(e)}"


# ----------------------------------------
# Text to Speech
# ----------------------------------------

def text_to_speech(text):
    try:
        tts = gTTS(text=text, lang="en")

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        ) as fp:
            tts.save(fp.name)
            return fp.name

    except Exception as e:
        print(e)
        return None


# ----------------------------------------
# Main Assistant
# ----------------------------------------

def voice_assistant(audio):
    if audio is None:
        return "No audio received.", "", None

    user_text = speech_to_text(audio)

    ai_reply = ask_gemini(user_text)

    voice_file = text_to_speech(ai_reply)

    return user_text, ai_reply, voice_file


# ----------------------------------------
# Gradio Interface
# ----------------------------------------

demo = gr.Interface(
    fn=voice_assistant,
    inputs=gr.Audio(
        type="filepath",
        label="🎤 Speak Here"
    ),
    outputs=[
        gr.Textbox(label="🗣 You Said"),
        gr.Textbox(label="🤖 Gemini Response"),
        gr.Audio(label="🔊 AI Voice"),
    ],
    title="🎙 AI Voice Assistant",
    description="Speak to Gemini AI and receive both text and spoken responses.",
    theme=gr.themes.Soft(),
)


if __name__ == "__main__":
    demo.launch(debug=True)
