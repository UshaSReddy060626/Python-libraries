from transformers import pipeline
summarizer = pipeline("summarization")
text = """
Artificial Intelligence is changing many industries.
It helps doctors diagnose diseases.
It helps students learn.
It powers self-driving cars.
"""
summary = summarizer(
    text,
    max_length=30,
    min_length=10)
print(summary[0]["summary_text"])