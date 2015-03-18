def calculate_coins(sum):
    result = {}
    coins = [100, 50, 20, 10, 5, 2, 1]
    # закръгляме числото
    sum = round(sum * 100)
    for coin in coins:
        count = sum // coin
        result[coin] = count
        sum -= count * coin
    return result

print(calculate_coins(8.94))
print(calculate_coins(0.53))
    
