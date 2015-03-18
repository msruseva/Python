name = input("Enter first name: ")
s_name = input("Enter second name: ")
t_name = input("Enter third name: ")
birth = input("Entwer birth year: ")
birth = int(birth)


current_age = 2015 - birth

person = {
    "first_name": name,
    "second_name": s_name,
    "third_name": t_name,
    "birth_year": birth,
    "current_age": current_age,
}

print(person)
