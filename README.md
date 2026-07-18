# 🎙️ AI Voice Assistant

An AI-powered Voice Assistant built using **Google Gemini AI**, **Gradio**, **SpeechRecognition**, and **gTTS**. Speak to the assistant through your microphone, and it will convert your speech to text, generate an intelligent response using Gemini AI, and reply with both text and voice.

## 🚀 Features

- 🎤 Speech-to-Text conversion
- 🤖 AI-powered responses using Google Gemini
- 🔊 Text-to-Speech output
- 🖥️ Interactive Gradio web interface
- 🌐 Simple and easy to use

## 🛠️ Technologies Used

- Python
- Google Gemini AI (`google-genai`)
- Gradio
- SpeechRecognition
- gTTS

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/fazilaanjum/ai-voice-assistant.git
cd ai-voice-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your Gemini API Key

#### Windows (Command Prompt)

```cmd
set GEMINI_API_KEY=YOUR_API_KEY
```

#### Windows (PowerShell)

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

#### Linux / macOS

```bash
export GEMINI_API_KEY=YOUR_API_KEY
```

### 4. Run the application

```bash
python app.py
```

The application will launch a local Gradio interface in your browser.

---

## 📸 How to Use

1. Launch the application.
2. Click the microphone or upload a voice recording.
3. Speak your question.
4. The application converts your speech into text.
5. Gemini AI generates an intelligent response.
6. The response is displayed as text and played back as audio.

---

## 📁 Project Structure

```
AI-Voice-Assistant/
│── app.py
│── requirements.txt
│── README.md
```

---

## ⚠️ Security

Never hardcode your Gemini API key in your source code or upload it to GitHub.

Use an environment variable instead:

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome. Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed with **Python**, **Google Gemini AI**, **Gradio**, **SpeechRecognition**, and **gTTS**.
