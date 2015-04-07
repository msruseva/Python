def is_string_palindrom(string):
    delete_objects = [" ", ",", ".", "!", "?"]
    temp = ""
    result = ""
    string = string.lower()
    
    for i in range(0, len(string)):
        if string[i] not in delete_objects:
            temp += string[i]

    for i in range(0, len(temp)):
        result = temp[i] + result

    if result == temp:
        return True
    
    return False
