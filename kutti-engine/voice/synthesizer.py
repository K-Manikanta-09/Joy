import edge_tts
import asyncio
import tempfile


class Synthesizer:

    async def generate(self, text, voice):

        file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )

        communicate = edge_tts.Communicate(
            text=text,
            voice=voice
        )

        await communicate.save(file.name)

        return file.name