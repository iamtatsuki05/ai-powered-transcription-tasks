import tiktoken


def calc_token_length(text: str, model: str = "gpt-3.5-turbo"):
    tokenizer = tiktoken.encoding_for_model(model)
    return len(tokenizer.encode(text))
