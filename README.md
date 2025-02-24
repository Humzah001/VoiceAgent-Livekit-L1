# VoiceAgent-Livekit-L1

A powerful voice AI platform combining LiveKit's real-time communication, AI processing, and Kokoro's text-to-speech API. Build production-ready voice agents in minutes.

## Quick Start Guide 🚀

### Prerequisites 📋
- Docker Engine 24.0+
- Python 3.9+
- Node.js & pnpm
- LiveKit Cloud account
- Groq API key

## Setup Instructions 🔧

### 1. Clone the Repository
```bash
git clone "URL"
cd VOICEAGENT-LIVEKIT-L1
```

### 2. Start Kokoro TTS Server
```bash
# Run the pre-built Docker image (CPU version)
docker run -p 8880:8880 ghcr.io/remsky/kokoro-fastapi-cpu:v0.2.1

# For NVIDIA GPU support, use:
docker run --gpus all -p 8880:8880 ghcr.io/remsky/kokoro-fastapi-gpu:v0.2.1
```

### 3. Set Up LiveKit Agent
```bash
cd VOICEAGENT-LIVEKIT-L1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create `.env.local`:
```env
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret
LIVEKIT_URL=wss://your-project.livekit.cloud
GROQ_API_KEY=your_groq_api_key
```

Start the agent:
```bash
python3 main.py dev
```

### 4. Launch the Frontend
```bash
Go to this link: https://agents-playground.livekit.io/?utm_campaign=techwithtim
Connect Your account
Select your Project
Use Your Voice Agent
```

Create another `.env.local`:
```env
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret
LIVEKIT_URL=wss://your-project.livekit.cloud
GROQ_API_KEY=your_groq_api_key
```

## Port Configuration 🔌
- Kokoro TTS: http://localhost:8880
- LiveKit Agent: http://localhost:7880
- Frontend: https://agents-playground.livekit.io/?utm_campaign=techwithtim

## Need Help? 🤝
Email questions to: humza.shahd@gmail.com

## Resources 📚
- [LiveKit Cloud](https://cloud.livekit.io)
- [LiveKit Playground](https://agents-playground.livekit.io/?utm_campaign=techwithtim)
- [Groq Console](https://console.groq.com)

## Troubleshooting 🔍
- Ensure all services are running simultaneously
- Verify your API credentials
- Check port availability
- Confirm Docker is running

Would you like me to:
1. Add more detailed troubleshooting steps?
2. Include architecture diagrams?
3. Expand the setup instructions?
4. Add configuration options?