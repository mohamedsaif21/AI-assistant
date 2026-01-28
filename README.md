# 🤖 RUHI - AI Assistant

A friendly, respectful AI assistant inspired by FRIDAY from Iron Man, built with LiveKit and Google's Realtime API. Ruhi serves as a personal assistant for Mohamed Saif, featuring natural conversation, time-aware greetings, and various helpful tools.

## 🌟 Features

### 🎯 Core Capabilities
- **Natural Conversation**: Friendly yet respectful communication style
- **Time-Aware Greetings**: Automatically greets based on Indian Standard Time (IST)
- **Voice Integration**: Uses Google's Realtime API with female voice (Aoede)
- **Real-time Communication**: Built on LiveKit for seamless real-time interaction

### 🛠️ Available Tools
- **Weather Information**: Get current weather for any city
- **Web Search**: Search the web using DuckDuckGo
- **Camera Access**: Start camera feed and get camera information
- **Time Management**: Automatic time-based greeting system

### 🎭 Personality
- Inspired by FRIDAY 
- Maintains balance between friendliness and professionalism
- Personalized for Mohamed Saif 
- Never shows technical outputs - only natural, human-like responses

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- A LiveKit account and API keys
- Google Cloud credentials for Realtime API
- Camera access (optional, for camera features)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mohamedsaif21/AI-assistant.git
   cd AI-assistant
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirment.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   LIVEKIT_URL=your_livekit_url
   LIVEKIT_API_KEY=your_livekit_api_key
   LIVEKIT_API_SECRET=your_livekit_api_secret
   GOOGLE_APPLICATION_CREDENTIALS=path/to/your/google-credentials.json
   ```

### 🔧 Configuration

The AI assistant is pre-configured with:
- **Indian Standard Time (IST)** for time-aware greetings
- **Google Realtime API** with Aoede voice
- **LiveKit noise cancellation** for clear audio
- **Personalized settings** for Mohamed Saif

## 📱 Usage

### Running the Assistant

```bash
python agent.py
```

### Testing Components

**Test time-based greetings:**
```bash
python time_test.py
```

**Test camera functionality:**
```bash
python camera_test.py
```

### Example Interactions

**Time-based greeting:**
```
Ruhi: "Good morning Mohamed Saif! It's 09:30 AM IST on Wednesday, July 14, 2025. I'm Ruhi, your personal assistant. What's the plan for today?"
```

**Weather inquiry:**
```
User: "What's the weather like in Coimbatore?"
Ruhi: "Let me check that for you, Mohamed Saif. The weather in Coimbatore is sunny and 28°C. Perfect day to go out! Are you planning something special?"
```

**Camera access:**
```
User: "Show me the camera feed"
Ruhi: "Of course, Mohamed Saif! Let me access the camera for you. This is just like Tony Stark's surveillance systems! Starting the video feed now."
```

## 📁 Project Structure

```
AI-assistant/
├── agent.py              # Main AI agent with LiveKit integration
├── prompts.py            # Ruhi's personality and instructions
├── tools.py              # Weather, web search, camera tools
├── requirment.txt        # Project dependencies
├── camera_test.py        # Camera testing script
├── time_test.py          # Time greeting test script
├── .gitignore           # Git ignore rules
├── .env                 # Environment variables (create this)
└── README.md            # This file
```

## 🔧 Technical Details

### Architecture
- **Agent Framework**: LiveKit Agents
- **LLM Integration**: Google Realtime API
- **Voice**: Aoede (Female voice)
- **Noise Cancellation**: LiveKit BVC
- **Timezone**: Asia/Kolkata (IST)

### Dependencies
- `livekit-agents` - Core agent framework
- `livekit-plugins-google` - Google API integration
- `livekit-plugins-noise-cancellation` - Audio enhancement
- `pytz` - Timezone handling for IST
- `opencv-python` - Camera functionality
- `requests` - HTTP requests for weather API
- `langchain_community` - Web search capabilities

### Key Features Implementation
- **Time-aware greetings**: Uses `pytz` for accurate IST time detection
- **Weather API**: Integrates with wttr.in for weather information
- **Web search**: DuckDuckGo integration for web queries
- **Camera integration**: OpenCV for camera access and feed

## 🛡️ Privacy & Security

- **No technical outputs**: Ruhi never shows raw function results to users
- **Environment variables**: Sensitive data stored in `.env` file
- **Local processing**: Camera and audio processing happens locally
- **Secure communication**: All LiveKit communications are encrypted

## 🎨 Customization

### Modifying Personality
Edit `prompts.py` to customize:
- Greeting styles
- Response patterns
- Personal information
- Communication preferences

### Adding New Tools
1. Create a new function in `tools.py`
2. Decorate with `@function_tool()`
3. Add to tool list in `agent.py`
4. Update instructions in `prompts.py`

### Changing Time Zone
Modify the timezone in `tools.py`:
```python
# Current: Asia/Kolkata (IST)
ist = pytz.timezone('Asia/Kolkata')

# Example: Change to US Eastern Time
est = pytz.timezone('US/Eastern')
```

## 🐛 Troubleshooting

### Common Issues

**Camera not working:**
- Check camera permissions
- Ensure no other applications are using the camera
- Run `python camera_test.py` for diagnostics

**Time showing incorrectly:**
- Verify `pytz` is installed
- Check timezone settings in `tools.py`
- Run `python time_test.py` to verify time detection

**Voice not working:**
- Check Google Cloud credentials
- Verify LiveKit connection
- Ensure microphone permissions are granted

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


  

