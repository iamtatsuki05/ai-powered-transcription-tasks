import tiktoken
from tiktoken.core import Encoding


def calc_token_length(text: str, model: str = "gpt-3.5-turbo"):
    tokenizer = Encoding.load(model)
    return len(tokenizer.encode(text))
