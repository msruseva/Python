def status_count(students):
    result = {
        "finalized": [],
        "not_finalized": []
        }
    
    for student in students:
        if student["status"] == "finalized":
            result["finalized"] += [student["name"]]
        else:
            result["not_finalized"] += [student["name"]]
            
    return result
