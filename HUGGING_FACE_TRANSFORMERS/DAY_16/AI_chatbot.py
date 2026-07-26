from transformers import pipeline
chatbot = pipeline(
    "text-generation",
    model="gpt2")
while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    reply = chatbot(
        user,
        max_new_tokens=40)
    print("\nBot:", reply[0]["generated_text"])