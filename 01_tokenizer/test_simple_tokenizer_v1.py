
from vocabulary import VOCAB_V1


# read the text file
raw_text = """"It's the last he painted, you know," 
       Mrs. Gisburn said with pardonable pride."""


# create an instance of the SimpleTokenizerV1 class with the vocabulary
from simple_tokenizer_v1 import SimpleTokenizerV1

tokenizer = SimpleTokenizerV1(VOCAB_V1)

token_ids = tokenizer.encode(raw_text) # tokenize the text and get the token IDs
print(f"Token IDs: {token_ids}")

# decode the token IDs back to text
decoded_text = tokenizer.decode(token_ids)
print(f"Decoded text: {decoded_text}")

