import os
from typing import Union
from pathlib import Path

import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def whisper_interface(audio_file_path:Union[str, Path], model_name:str = "whisper-1", **kwargs):
    audio_file = open(audio_file_path, "rb")
    completion = openai.Audio.create(
        file=audio_file,
        model=model_name,
        **kwargs
    )
    return completion.choices[0].text
