from transformers import pipeline
classifier = pipeline(
    "sentiment-analysis"
)
print(classifier("I love learning AI."))
print(classifier("This is the worst day ever."))