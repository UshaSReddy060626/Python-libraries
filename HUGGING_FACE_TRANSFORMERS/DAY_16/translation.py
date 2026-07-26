from transformers import pipeline
translator = pipeline(
    "translation_en_to_fr")
result = translator(
    "Machine Learning is amazing.")
print(result)