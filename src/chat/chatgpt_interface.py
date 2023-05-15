import os

import openai
openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_gpt_interface(context:str, model_name:str = "gpt-3.5-turbo", **kwargs):
    completion = openai.ChatCompletion.create(
        model=model_name,
        messages=[{"role": "user", "content": context}],
        **kwargs
    )
    return completion.choices[0].message.content
