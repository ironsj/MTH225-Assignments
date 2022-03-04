def union(A, B):  # creates union function with lists A & B as arguments
    union_list = []  # creates list that will be union of A & B
    for element in (A + B):  # goes through each element in A & B
        if element not in union_list:  # creates condition for anything not in the list already
            union_list.append(element)  # adds elements to the final list (A or B)
            union_list.sort()  # sorts list in ascending order
    return union_list  # returns the final list


def intersect(A, B):  # creates intersect funtion with lists A & B as arguments
    temp_list = []  # creates temporary list to be used in the function
    intersect_list = []  # creates list that will be intersection of A & B
    for element in A:  # goes through elements of A
        if element in B:  # creates a condition that makes it so element must also be in B
            temp_list.append(element)  # adds elements to temporary list
    for element in temp_list:  # goes through elements in the temporary list
        if element not in intersect_list:  # creates a condition for anything not in list already
            intersect_list.append(element)  # adds elements to final list
            intersect_list.sort()  # sorts list in ascending order
    return intersect_list  # returns the final list


def equal(A, B):  # creates a function that checks if A & B are equal
    return_value = False  # creates our return value
    if sorted(A) == sorted(B):  # creates condition that the A and B in numerical order are equal
        return_value = True  # if the condition hold true then the value is true
    else:  # states what happens when the above condition isn't true
        return_value = False  # all other cases are false
    return return_value  # returns the boolean value

A = [0,1,2,3]
B= [0,1,2,4]
print(equal(A, B))
