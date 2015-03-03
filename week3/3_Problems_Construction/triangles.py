def is_triangle(a, b, c):
    if (a + b) > c and (b + c) > a and (a + c) > b:
        return True
    else:
        return False

def area(a, b, c):
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
    return S
    
def is_pythagorean(a, b , c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False

def max_area(triangles):
    current_max = triangles[0]
    a = current_max[0]
    b = current_max[1]
    c = current_max[2]
    current_max_area = area(a, b, c)
    for i in triangles:
        a = i[0]
        b = i[1]
        c = i[2]
        current_area = area(a, b, c)
        if current_area > current_max_area:
            current_max = i
            current_max_area = current_area
    
    return current_max
