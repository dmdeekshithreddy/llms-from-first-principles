from vocabulary import VOCAB_V2
from simple_tokenizer_v2 import SimpleTokenizerV2
from itertools import islice

# input text for testing
text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."

text = " <|endoftext|> ".join([text1, text2])
print(f"Input text: {text}")

print(f"Last 5 tokens in the Vocabulary: {list(VOCAB_V2.items())[-5:]}") # print the last 5 tokens in the vocabulary
# create an instance of the SimpleTokenizerV2 class with the vocabulary
tokenizer = SimpleTokenizerV2(VOCAB_V2)

# encode the text and get the token IDs
token_ids = tokenizer.encode(text)
print(f"Token IDs: {token_ids}")

# decode the token IDs back to text
decoded_text = tokenizer.decode(token_ids)
print(f"Decoded text: {decoded_text}")

