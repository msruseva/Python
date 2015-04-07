def taken_name(surname_husband, surname_wife):
    
    for ch in range(0, len(surname_husband)):
        if surname_husband in surname_wife:
            return True
        
    return False
