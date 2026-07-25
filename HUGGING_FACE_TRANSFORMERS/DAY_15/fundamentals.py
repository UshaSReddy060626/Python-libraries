#sentiment analysis
import os
os.environ["HF_TOKEN"] = "your_actual_token_here"
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("I love Learning AI")
print(result)

#text generation
generator=pipeline("text-generation")
result=generator("artifical intelligence is", max_new_tokens=20)
print(result)