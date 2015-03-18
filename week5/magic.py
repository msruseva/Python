def sum_main_diagonal(numbers):
    index = 0
    sum_main = 0
    
    while index < len(numbers):
        sum_main = sum_main + numbers[index][index]
        index += 1

    return sum_main

def sum_second_diagonal(numbers):
    row_index = 0
    col_index = len(numbers) - 1
    sum_second = 0

    for row in numbers:
        sum_second = sum_second + numbers[row_index][col_index]
        row_index += 1
        col_index -= 1

    return sum_second

def sum_coloms(numbers, index):
    sum_coloms = 0

    for row in numbers:
        sum_coloms = sum_coloms + row[index]

    return sum_coloms
    
def sum_row(numbers, index):
    sum_row = 0
    
    for row in numbers:
        sum_row = sum_row + row[index]
        
    return sum_row
   
def magic_square(square):
    sum_square = sum_main_diagonal(square)

    if sum_second_diagonal(square) != sum_square:
        return False

    for index in range(0, len(square)):
        if sum_row(square, index) != sum_square:
            return False

    for index in range(0, len(square)):
        if sum_coloms(square, index) != sum_square:
            return False

    return True

            
