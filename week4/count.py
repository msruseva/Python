def count_vowels_consonants(word):
    result = {
        "vowels": 0,
        "consonants": 0
    }
    vowels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxwzBCDFGHJKLMNPQRSTVWXZ"
    for i in word:
        if i in vowels:
            result["vowels"] += 1
        elif i in consonants:
            result["consonants"] += 1
    return result

print(count_vowels_consonants("aaaAcccD"))
            
