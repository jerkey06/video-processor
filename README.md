# Video Processor

The Video Processor is a Python-based application designed for the automated analysis and concise editing of video files. It leverages advanced speech detection, transcription, and artificial intelligence to identify and eliminate redundant content, thereby preserving the core informational value of the video.

## Features

- **Automated Speech Detection:** Identifies spoken content within video files.
- **Multi-Provider Audio Transcription:** Supports transcription services from leading AI providers:
    - OpenAI (Whisper)
    - DeepSeek Audio
    - Google Gemini Pro
- **Intelligent Content Filtering:** Employs sophisticated AI models for content refinement:
    - GPT-4
    - DeepSeek Chat
    - Gemini Pro
- **Automated Video Editing and Compilation:** Streamlines the process of video segment selection and assembly.
- **Broad Format Compatibility:** Supports common video formats including `.mp4`, `.mov`, `.avi`, and `.mkv`.

## Project Structure

```
video_processor/
├── requirements.txt         # Project dependencies
├── .env                     # Environment variables
├── README.md                # Project documentation
├── src/                     # Source code directory
│   ├── main.py              # Application entry point
│   ├── config.py            # Configuration settings
│   ├── services/            # Core service modules
│   │   ├── audio_service.py         # Audio processing functionalities
│   │   ├── transcription_service.py # Audio transcription services
│   │   ├── llm_service.py           # AI-driven content filtering
│   │   └── video_service.py         # Video editing and manipulation
│   └── utils/               # Utility functions
│       └── file_utils.py
├── raw/                     # Directory for input video files
└── edited/                  # Directory for processed video outputs
```

## Prerequisites

- Python 3.8 or higher
- FFmpeg installed and accessible in the system's PATH
- Valid API key for OpenAI, DeepSeek, or Google Gemini

## Installation

1. Clone the repository:

Bash

```
git clone https://github.com/jerkey06/video-processor.git
cd video-processor
```

2. Create and activate a virtual environment:

Bash

```
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. Install project dependencies:

Bash

```
pip install -r requirements.txt
```

4. API Configuration:

### Option 1: OpenAI API

1. Navigate to [OpenAI's platform](https://platform.openai.com/account/api-keys)
2. Register or log in
3. Access "API Keys" from the sidebar
4. Click "Create new secret key"
5. Copy the generated key

### Option 2: DeepSeek API

1. Navigate to [DeepSeek's platform](https://platform.deepseek.com/)
2. Create an account and log in
3. Go to the "API Keys" section
4. Generate a new API key

### Option 3: Google Gemini API

1. Navigate to [Google AI Studio](https://makersuite.google.com/app/apikey)
    
2. Log in with your Google account
    
3. Click "Get API key"
    
4. Create a new API key or utilize an existing one
    
5. Create a `.env` file in the project root directory and populate it with the required API keys:
    

```
OPENAI_API_KEY=your_api_key_here
DEEPSEEK_API_KEY=your_api_key_here
GEMINI_API_KEY=your_api_key_here
```

## Usage

1. Configure the desired AI provider in `src/config.py`:

Python

```
class Config:
    AI_PROVIDER = "openai"  # Options: "openai", "deepseek", "gemini"
```

2. Place your video files into the `raw/` directory.
    
3. Execute the video processor:
    

Bash

```
python src/main.py
```

4. Retrieve the processed video files from the `edited/` directory.

## API Pricing Comparison

### OpenAI

- Whisper API: $0.006 per minute
- GPT-4: Starting from $0.03 per 1K tokens

### DeepSeek

- Audio Transcription: $0.004 per minute
- Chat Model: Starting from $0.001 per 1K tokens

### Google Gemini

- Gemini Pro: $0.00025 per 1K tokens (Free up to a certain usage threshold!)
- Audio Processing: Included in the base price

_Note: Pricing is subject to change. Refer to the official provider websites for current rates:_

- [OpenAI Pricing](https://openai.com/pricing)
- [DeepSeek Pricing](https://platform.deepseek.com/pricing)
- [Google AI Pricing](https://ai.google.dev/pricing)

## Troubleshooting

### FFmpeg Not Found

- Ensure FFmpeg is installed and its executable path is included in the system's PATH environment variable.
- Windows: Download and install from ffmpeg.org
- macOS: `brew install ffmpeg`
- Linux: `sudo apt-get install ffmpeg`

### OpenAI API Errors

- "Insufficient quota": Verify your usage limits and billing status.
- "Rate limit reached": Await a few minutes or request an increase in your rate limits.
- "Invalid API key": Reconfirm the accuracy of your API key in the `.env` file.

### DeepSeek API Errors

- "Authentication failed": Verify that your API key is correctly copied.
- "Quota exceeded": Review your DeepSeek account balance.
- "Model not available": Ensure the correct model names are being used.

### Gemini API Errors

- "API key not valid": Confirm that your Google API key is active.
- "Quota exceeded": Review your free usage limits.
- "Region not supported": Verify service availability in your geographical region.

### Memory Issues

- Consider processing video segments of shorter durations.
- Ensure adequate system memory resources are available.
- Terminate other memory-intensive applications.

## Contribution

To contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature.
3. Implement your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License. Refer to the LICENSE file for detailed information.

## Acknowledgments

This project incorporates various open-source libraries and APIs:

- OpenAI Whisper and GPT
- DeepSeek Audio and Chat
- WebRTC VAD
- MoviePy
- pydub
- LangChain

