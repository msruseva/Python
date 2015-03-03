from random import randint

n = input("Enter dice side: ")
n = int(n)

first_player = input("Enter player1 name: ")
second_player = input("Enter player2 name: ")

dice_first = randint(1,n)
print(first_player + " " + str(dice_first))
dice_second = randint(1,n)
print(second_player + " " + str(dice_second))

if dice_first > dice_second:
    print(first_player + " wins!")
elif dice_second > dice_first:
    print(second_player + " wins!")
elif dice_first == dice_second:
    print("There is no winner. Players are equal.")

