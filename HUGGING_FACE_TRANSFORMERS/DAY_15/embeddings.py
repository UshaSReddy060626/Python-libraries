#import required libraries
from transformers import AutoTokenizer
from transformers import AutoModel
import torch

#load tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "distilbert-base-uncased"
)

#load pretrained model
model = AutoModel.from_pretrained(
    "distilbert-base-uncased"
)

#input sentence
sentence = "I love learning Artificial Intelligence."

#tokenize sentence
inputs = tokenizer(
    sentence,
    return_tensors="pt"
)

#get model output
with torch.no_grad():
    outputs = model(**inputs)

#hidden states
hidden_states = outputs.last_hidden_state

print("Hidden States:")
print(hidden_states)

#sentence embedding
sentence_embedding = hidden_states.mean(dim=1)

print("\nSentence Embedding:")
print(sentence_embedding)

#embedding shape
print("\nEmbedding Shape:")
print(sentence_embedding.shape)