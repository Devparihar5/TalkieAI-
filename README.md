# TalkieAI 📽️ : Talk with your Video

## Description
Interact with videos like never before! Upload or paste a YouTube link, and our app processes the audio, transcribes it, and lets you chat directly with your video content using cutting-edge language models.

## Features
- Upload or paste a YouTube link to fetch your video.
- Process the audio from the video and transcribe it using advanced models.
- Engage in conversation directly with your video content.

## Installation

### Clone the repository and navigate to the directory

```bash
git clone https://github.com/Devparihar5/TalkieAI-.git
```

```bash
cd TalkieAI-
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

<details>
  <summary>Windows</summary>

```pwsh
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

```pwsh
.\venv\Scripts\activate.ps1
```

</details>

<details>
  <summary>GNU/Linux or macOS</summary>

```bash
source venv/bin/activate
```

</details>

### Upgrade pip and install the dependencies

```bash
python -m pip install -U pip
```

```bash
pip install -r requirements.txt
```

### Run the server

```bash
streamlit run Upload_Your_Video.py
```

Feel free to engage with your videos in a whole new way with TalkieAI!
