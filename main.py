import asyncio

from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero

load_dotenv()

async def entrypoint(ctx: JobContext):
    initial_ctx = llm.ChatContext().append(
    role="system",
    text=(
        "You are a voice assistant created by Hamza the AI Expert. Your interface with users will be voice. "
        "You should use short and concise responses, and avoiding usage of unpronouncable punctuation. "
    ),
    )
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # Initialize OpenAI TTS plugin with Kokoro settings, but using tts-1 model name
    kokoro_tts = openai.TTS(
        model="tts-1",  # Use tts-1 to be compatible with LiveKit
        voice="am_michael", # Select a voice - see available voices at http://localhost:8880/v1/audio/voices
        api_key="not-needed", #Not needed for local instance
        base_url="http://localhost:8880/v1"  # Point to Kokoro FastAPI endpoint
    )

    agent = VoiceAssistant(
        # vad=ctx.proc.userdata["vad"],
        vad=silero.VAD.load(),
        stt=openai.STT.with_groq(model="distil-whisper-large-v3-en"),
        llm=openai.LLM.with_groq(model="llama-3.3-70b-versatile"),
        tts=kokoro_tts,  # Use Kokoro TTS (through OpenAI-compatible endpoint)
        chat_ctx=initial_ctx,
    )

    agent.start(ctx.room)

    await asyncio.sleep(1)
    # The agent should be polite and greet the user when it joins :)
    await agent.say("Hey, how can I help you today?", allow_interruptions=True)

if __name__ == '__main__':
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))