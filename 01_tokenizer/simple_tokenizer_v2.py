import re
from vocabulary import SPCL_TOKENS

class SimpleTokenizerV2:
    # split the text based on either of the below symbols defined below in the pattern.
    special_tokens = "|".join(re.escape(t) for t in SPCL_TOKENS) # o/p: <\|endoftext\|>|<\|unk\|>
    PATTERN = re.compile(r"(" + special_tokens + r"|--|\s|[^a-zA-Z0-9\-])")

    def __init__(self, vocab):
        self.token_to_id = vocab # dict of token to token_id
        self.id_to_token = {token_id: token for token, token_id in vocab.items()} # dict of token_id to token

    def encode(self, text: str) -> list[int]:
        tokens = [t for t in self.PATTERN.split(text) if t] # split the text based on the pattern and filter out empty tokens
        unk_id = self.token_to_id["<|unk|>"] # get the token ID for the unknown token
        return [self.token_to_id.get(t, unk_id) for t in tokens]

    def decode(self, token_ids: list[int]) -> str:
        return "".join(self.id_to_token[i] for i in token_ids)

