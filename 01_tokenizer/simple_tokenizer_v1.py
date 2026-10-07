# Step 4: Create SimpleTokenizerV1 class

# SimpleTokenizerV1 will have two methods
# 1. encode (to convert tokens to token IDs)
# 2. decode (to convert token IDs to tokens)

import re

class SimpleTokenizerV1:
    PATTERN = re.compile(r'(--|[^a-zA-Z0-9\s]|\s)')

    def __init__(self, vocab):
        self.token_to_id = vocab # dict of token to token_id
        self.id_to_token = {token_id: token for token, token_id in vocab.items()} # dict of token_id to token

    def encode(self, text: str) -> list[int]:
        tokens = [t for t in self.PATTERN.split(text) if t]
        return [self.token_to_id[t] for t in tokens]

    def decode(self, token_ids: list[int]) -> str:
        return "".join(self.id_to_token[i] for i in token_ids)
