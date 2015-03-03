import time
today = time.strftime("%A")
print(today)

if today == "Friday":
    print("It is Friday!")
else:
    print("It is not Friday ;( Today is " + today)
