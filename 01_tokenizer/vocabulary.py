import re
from pathlib import Path

def build_simple_vocab(text: str) -> dict:
    PATTERN = re.compile(r'(--|[^a-zA-Z0-9\s]|\s)')
    tokens = [t for t in PATTERN.split(text) if t] # split based on the pattern and filter out empty tokens
    unique_tokens = sorted(set(tokens)) # remove duplicates and sort the tokens
    return {token: i for i, token in enumerate(unique_tokens)}

# add `<|endoftext|>` and `<|unk|>` tokens to the vocabulary
def build_simple_vocab_v2(text: str) -> dict:
    PATTERN = re.compile(r'(--|[^a-zA-Z0-9\s]|\s)')
    SPCL_TOKENS = ["<|endoftext|>", "<|unk|>"]

    tokens = [t for t in PATTERN.split(text) if t]
    unique_tokens = sorted(set(tokens))
    unique_tokens.extend(SPCL_TOKENS)
    return {token: i for i, token in enumerate(unique_tokens)}




# build vocabulary once from the text file and reuse it in both SimpleTokenizerV1 and SimpleTokenizerV2
text_file = Path(__file__).resolve().parent.parent / "datasets" / "the-verdict.txt"

with open(text_file, "r", encoding="utf-8") as f:
    raw_text = f.read()

VOCAB_V1 = build_simple_vocab(raw_text)
VOCAB_V2 = build_simple_vocab_v2(raw_text)



