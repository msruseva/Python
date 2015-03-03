def lylin_city(blocks):
    if len(blocks) == 0:
        return 0
    count_blocks = 0
    high_block = blocks[0]
    for block in blocks:
        if block >= high_block:
            count_blocks += 1
            high_block = block
            
    return count_blocks

n = input("Enter n: ")
n = int(n)

blocks = []
start = 1

while start <= n:
    high = input("Enter high of the blocks: ")
    high = int(high)
    blocks = blocks + [high]
    start += 1

print(lylin_city(blocks))
