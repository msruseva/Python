def sublist(list1, list2):
    list_index = 0
    sublist_index = 0
    temp_list = []
    
    while list_index < len(list2):
        sublist_index = list_index
        while sublist_index < len(list1):
            temp_list += [list2[sublist_index]]
            sublist_index += 1
        if temp_list == []:
            return True
        elif temp_list == list1:
            return True
        temp_list = []
        list_index += 1
        
    return False
