from transformers import pipeline
qa = pipeline("question-answering")
result = qa(question="What is the capital of France?",
context="""
France is a country in Europe.
Its capital is Paris.
""")
print(result)