def string_matrix(matrix_width, strings):
    result = ""
    delimiter = " | "


    for i in range(0,len(strings) - 1):
        result += "| "
        for j in range(0, matrix_width):
            if j >= len(strings[i]):
                result += "X"
                result += delimiter
            else:
                result += strings[i][j]
                result += delimiter
        result += "\n"

    result += "| "
    for j in range(0, len(strings)):
        result += strings[len(strings) - 1][j]
        result += delimiter
        
    print(result)           
