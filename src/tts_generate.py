import edge_tts
import asyncio


async def synthesize_audio(text, output_path, voice="en-US-AriaNeural"):
    try:
        communicate = edge_tts.Communicate(text, voice=voice)
        await communicate.save(output_path)
    except Exception as e:
        print(f"❌ Edge TTS failed: {e}")
        raise e


def generate_audio(text, output_path, voice="en-US-AriaNeural"):
    asyncio.run(synthesize_audio(text, output_path, voice))