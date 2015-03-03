from random import randint

n = input("Enter sides: ")
n = int(n)

dice_one = randint(1,n)
dice_two = randint(1,n)
sum = dice_one + dice_two

print("First roll:")
print(dice_one)
print("Second roll:")
print(dice_two)
print("Sum is:")
print(sum)
