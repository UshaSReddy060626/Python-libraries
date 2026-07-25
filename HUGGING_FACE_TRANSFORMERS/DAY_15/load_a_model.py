#import required libraries
from transformers import AutoTokenizer
from transformers import AutoModel

#load tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "distilbert-base-uncased"
)

#load pretrained model
model = AutoModel.from_pretrained(
    "distilbert-base-uncased"
)

#input sentence
sentence = "Artificial Intelligence is amazing."

#tokenize sentence
inputs = tokenizer(
    sentence,
    return_tensors="pt"
)

#pass input to model
outputs = model(**inputs)

#print model output
print("Model Output:")
print(outputs)