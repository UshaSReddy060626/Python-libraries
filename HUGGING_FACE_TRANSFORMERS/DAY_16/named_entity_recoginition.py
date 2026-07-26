from transformers import pipeline
ner = pipeline(
    "ner",
    grouped_entities=True)
result = ner(
    "Sundar Pichai works at Google in California.")
print(result)