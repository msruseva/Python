def helper(string):
    result = ""
    i = 0

    while string[i] == " ":
        i += 1

    for j in range(i, len(string)):
        result += string[j]
    return result

def reverse(string):
    result = ""
    
    for i in range(0, len(string)):
        result = string[i] + result
        
    return result

def inner_trim(string):
    string = reverse(helper(reverse(helper(string))))
    result = ""
    i = 0

    while i < len(string):
        if string[i] == " ":
            result += string[i]
            while string[i] == " ":
                i += 1
        else:
            result += string[i]
            i += 1

    return result
