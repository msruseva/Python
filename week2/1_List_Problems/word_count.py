string =  input("Enter word: ")
n = input ("Enter n: ")
n = int(n)

count = 1
words_list = []
br = 0

while count <= n:
    word = input("Enter word: ")
    words_list += [word]
    count += 1
for i in words_list:
    if string == i:
        br += 1
print(string + " is found " + str(br) + " times.")
