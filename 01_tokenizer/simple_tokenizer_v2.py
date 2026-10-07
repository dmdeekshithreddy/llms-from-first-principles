import re

class SimpleTokenizerV2:
    # split the text based on either of the below symbols defined below in the pattern.
    PATTERN = re.compile(r'(--|[^a-zA-Z0-9\-])')

    def __init__(self, vocab):
        self.token_to_id = vocab # dict of token to token_id
        self.id_to_token = {token_id: token for token, token_id in vocab.items()} # dict of token_id to token

    def encode(self, text: str) -> list[int]:
        tokens = [t if t in self.token_to_id else "<|unk|>" for t in self.PATTERN.split(text)]
        return [self.token_to_id[t] for t in tokens]

    def decode(self, token_ids: list[int]) -> str:
        return "".join(self.id_to_token[i] for i in token_ids)

