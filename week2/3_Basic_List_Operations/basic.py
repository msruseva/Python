one = [1]
three = [1,2,3]
empty = []
boolean = [True, True, True]
name = ["Mila", "Svetloslavova", "Ruseva"]
friends = ["Stani", "Ema", "Mariq", "Svetlin", "Victor"]
programming = ["C++", "Python", "Haskell", "Prolog"]


languages = ["Python", "Ruby"]
languages += ["C++", "Java", "C#"]
languages = ["Haskell"] + languages
languages += ["Go"]


print(languages[0])
print(languages[1])
print(languages[4])
languages[3] = "F#"
print(languages[3])
print(languages[len(languages) - 1])


if "Haskell" in languages:
    print("Yes, Haskell is in languages.")
else:
    print("No, Haskell is not in languages.")

if "Ruby" in languages:
    print("Yes, Ruby is in languages.")
else:
    print("No, Ruby is not in languages.")

if "Go" in languages:
    print("Yes, Go is in languages.")
else:
    print("No, Go is not in languages.")

if "Rust" in languages:
    print("Yes, Rust is in languages.")
else:
    print("No, Rust is not in languages.")


a = [1, 2, 3]
b = [4, 5, 6]
c = [1]
d = [8, 8, 10]

result = c + b + a + d
print(result)
a_b = a + b
print(a_b)
c_d = c + d
print(c_d)
a_a = a + a
print(a_a)




















