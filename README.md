# TalkieAI 📽️ : Talk with your Video

## Description
Interact with videos like never before! Upload or paste a YouTube link, and our app processes the audio, transcribes it, and lets you chat directly with your video content using cutting-edge language models.

## Features
- Upload or paste a YouTube link to fetch your video.
- Process the audio from the video and transcribe it using advanced models.
- Engage in conversation directly with your video content.

## Demo

### Fetch Video from YouTube
![Fetch Video from YouTube](https://github.com/Devparihar5/TalkieAI-/blob/main/images/video-upload.png)

### Chat with Your Video
![Chat with Your Video](https://github.com/Devparihar5/TalkieAI-/blob/main/images/chat.png)


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

### Set the Hugging Face API Token in secrets.toml

```bash
mkdir .streamlit
echo HUGGINGFACEHUB_API_TOKEN = "YOUR_HUGGING_FACE_API_TO_FETCH_MODELS" > .streamlit/secrets.toml
```
*Note: You can easily get your API Keys from [HuggingFace](https://huggingface.co/settings/tokens)*




### Run the server

```bash
streamlit run Upload_Your_Video.py
```

Feel free to engage with your videos in a whole new way with TalkieAI!

Replace `YOUR_HUGGING_FACE_API_TO_FETCH_MODELS` with your actual Hugging Face API token. This ensures that the token is directly set in the `.streamlit/secrets.toml` file during setup.


## Contributors

We welcome contributions from the community to enhance TalkieAI! If you'd like to contribute, please follow these steps:

1. Fork the repository [here](https://github.com/Devparihar5/TalkieAI-).
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name`.
4. Implement your changes and ensure they follow the project's coding style and guidelines.
5. Commit your changes: `git commit -m "Your descriptive commit message"`.
6. Push to the branch: `git push origin feature/your-feature-name`.
7. Submit a pull request to the main repository.
8. Wait for feedback and address any requested changes.

Thank you for being so interested in contributing to TalkieAI! Your contributions are highly appreciated.
