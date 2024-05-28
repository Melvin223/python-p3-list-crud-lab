def create_an_empty_list():
    return []

def create_a_list():
    my_list = [1, "apple", 3.14, True]
    return my_list

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    if l:  # Check if the list is not empty
        l.pop()
    return l

def remove_element_from_start_of_list(l):
    if l:  # Check if the list is not empty
        del l[0]
    return l

def retrieve_first_element_from_list(l):
    if l:  # Check if the list is not empty
        return l[0]
    else:
        return None  # Return None if the list is empty

def retrieve_element_from_index(l, index):
    if l and 0 <= index < len(l):  # Check if the list is not empty and if the index is within bounds
        return l[index]
    return None

def retrieve_last_element_from_list(l):
    if l:  # Check if the list is not empty
        return l[-1]
    else:
        return None
