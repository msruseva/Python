string = input("Enter text: ")

count = 0

for word in string:
    if word in "aeiouyAEIOUY":
        count += 1
        
print(count)
