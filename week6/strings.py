def join(delimiter, items):
    for i in range(0,len(items) - 1):
        items[i] += delimiter
    result = ""
    for item in items:
        result += item

    return result

def startswith(search, string):
    n_search = len(search)
    
    for i in range(0,n_search):
        if search[i] != string[i]:
            return False
        
    return True

def endswith(search, string):
    j = 0
    for i in range(len(string) - len(search), len(string)):
        if search[j] != string[i]:
            
            return False
        j += 1
    return True

def trim(string):
    temp = ""
    i = 0
    
    while i < len(string):
        if string[i] == " ":
            i += 1
        else:
            break
        
    for j in range(i, len(string)):
        temp = string[j] + temp

    result = ""
    i = 0

    while i < len(temp):
        if temp[i] == " ":
            i += 1
        else:
            break

    for j in range(i, len(temp)):
        result = temp[j] + result

    return result
        
