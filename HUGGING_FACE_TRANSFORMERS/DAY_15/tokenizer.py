from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
tokens = tokenizer.tokenize("I love AI")
print(tokens)

# encode
encoded = tokenizer.encode("I love AI")
print(encoded)

#decode
decoded = tokenizer.decode(encoded)
print(decoded)