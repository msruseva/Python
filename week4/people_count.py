def get_people_count(activity):
    people_in = []
    count = 0
    
    for item in activity:
        if item not in people_in:
            people_in += [item]
            count += 1
            
    return count

print(get_people_count(["Rado", "Ivo", "Maria", "Anneta", "Rado", "Rado", "Anneta", "Ivo", "Maria", "Rado"]))
