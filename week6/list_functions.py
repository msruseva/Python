def head(items):
    return items[0]

def last(items):
    last = len(items) - 1
    return items[last]

def tail(items):
    new = []
    index = 1
    
    while index < len(items):
        new += [items[index]]
        index += 1
        
    return new

def equal_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    
    for index in range(0, len(list1)):
        if list1[index] != list2[index]:
            return False

    return True
    
def count_item(n, items):
    result = 0
    index = 0
    
    while index < len(items):
        if n == items[index]:
            result += 1
        index += 1
            
    return result

def take(n, items):
    result = []

    for index in range(0, min(n, len(items))):
        result += [items[index]]
        
    return result

def drop(n, items):
    result = []

    for index in range(n, len(items)):
        result += [items[index]]

    return result

def reverse(items):
    result = []

    for item in items:
        result = [item] + result

    return result

















        
