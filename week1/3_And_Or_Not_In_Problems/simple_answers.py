text = input("Enter text: ")

if "hello" or "Hello" in text:
    print("Hello there, good stranger.")
elif "how are you?" in text:
    print("I'm fine, thanks. How are you?")
elif "feelings" in text:
    print("I am a machine. I kave no feelings.")
elif "age" in text:
    print("I have no age. Only current timestamp")
else:
    print(text)
