#import required libraries
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch

#load tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "distilbert-base-uncased"
)

#load sequence classification model
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=2
)

#input sentence
sentence = "I love learning AI."

#tokenize sentence
inputs = tokenizer(
     sentence,
    return_tensors="pt"
)

#pass input to model
with torch.no_grad():
    outputs = model(**inputs)

#print logits
print("Logits:")
print(outputs.logits)