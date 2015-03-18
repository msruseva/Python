def hash_them(keys, values):
    new_hash = {}
    index = 0 
    for key in keys:
        if index < len(values):
            # key - елементите в keys
            # index - елементите във values
            new_hash[key] = values[index] 
        else:
            new_hash[key] = None
        index += 1
    return new_hash

print(hash_them(["key"],["values"]))
print(hash_them(["key1", "key2"], ["value1"]))
