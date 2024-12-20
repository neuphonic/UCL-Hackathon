from pyneuphonic import Neuphonic, TTSConfig
from pyneuphonic.player import AudioPlayer
import os

api_key = "" # GET THIS FROM beta.neuphonic.com!!!!!!!!!

client = Neuphonic(api_key=api_key)
sse = client.tts.SSEClient()
tts_config = TTSConfig(speed=1.05,  voice='8e9c4bc8-3979-48ab-8626-df53befc2090', model="neu_hq")

with AudioPlayer() as player:
    response = sse.send("""Neuphonic generates high quality and low latency text to speech. Experience the speed and clarity of our dynamically powered voice synthesis by entering your text!""", tts_config=tts_config)
    player.play(response)
    # player.save_audio('output.wav') 