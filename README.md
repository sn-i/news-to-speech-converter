
# News-to-Speech Converter

**News-to-Speech Converter** is a web application that enables users to convert news articles from supported Georgian websites into audio format using Microsoft's Azure Text-to-Speech (TTS) API. With a simple, user-friendly interface, users can paste a URL of an article and receive an MP3 audio file, making news accessible for listening on the go.

[![Watch the video](https://img.youtube.com/vi/3-g6sGOvj_o/0.jpg)](https://youtu.be/3-g6sGOvj_o)

## Features

- **Convert News Articles to Audio**: Easily turn text from supported news articles into spoken-word audio files.
- **Microsoft Azure TTS Integration**: Leverages Azure's Text-to-Speech API for clear and natural-sounding audio.
- **Simple User Interface**: Clean, responsive design with intuitive input forms.
- **Error Handling and Notifications**: Displays messages for unsupported websites or issues with the input URL.
- **Downloadable MP3**: Offers a one-click download of the generated audio file.

## Supported Websites

This application currently supports the following popular Georgian news sites:

- [Mtavari TV](https://mtavari.tv)
- [Radio Tavisupleba](https://tavisupleba.org)
- [TV Pirveli](https://tvpirveli.ge)
- [Tabula GE](https://tabula.ge)
- [1TV](https://1tv.ge)

> **Note**: Only the listed websites are supported. Articles from other websites cannot be converted with this application at this time.

## Technologies Used

- Flask
- BeautifulSoup
- Microsoft Azure Text-to-Speech API
- CSS and HTML
- Python

## Installation

### Prerequisites

- **Python 3.7+**
- **Microsoft Azure Text-to-Speech API Key**
- **pip** (Python package installer)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sn-i/news-to-speech-converter.git
   cd news-to-speech-converter

   ```

2. **Set Up a Virtual Environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Keys**

   Sign up for Microsoft Azure and create a Cognitive Services resource to get an API key. Create a `.env` file in the root directory and add the following:

   ```env
   speech_key=your_azure_speech_key
   service_region=your_service_region
   ```

   Replace `your_azure_speech_key` and `your_service_region` with your Azure API credentials.

5. **Run the Application**

   ```bash
   flask run
   ```

6. **Access the Application**

   Open your web browser and go to `http://127.0.0.1:5000` to start using the app.

## Usage

1. **Enter a URL**: Paste a supported news article URL into the input field.
2. **Convert to Audio**: Click the "Convert to Audio" button to start processing.
3. **Download the MP3**: Once processed, download the generated audio file and enjoy listening.

---

Made by Sani Inauri ❤️
```
