def injective (f): #creates injective function with dictionary f as argument
    value = False #creates boolean value and sets to false
    range_list = [] #creates empty list that will hold range
    for key in f: #goes through each key in f
        range_list.append(f[key]) #adds value to range list
    if len(range_list) == len(set(range_list)): #creates condition that length of range list must be same length as range list with unique elements
        value = True #true if condition holds true
    else: #states what happens if condition is not true
        value = False #sets boolean to false if condition is not true
    return value #returns boolean value

def surjective(f, C): #creates surjective function with dictionary f and list C as arguments
    value = False #creates boolean value
    range_list = [] #creates empty list that will hold range
    for key in f: #goes through each key in f
        range_list.append(f[key]) #adds value to range list
    if len(C) == len(set(range_list)): #creates condition that length of C must be equal to length of range list with unique elements
        value = True #true if condition holds true
    else: #states what happens if condition is not true
        value = False #sets boolean to false if condition is not true
    return value #returns boolean value

def inverseImage(f, a): #creates inverseImage function with dictionary f and list of codomain values, a, as arguments
    inverse = [] #creates empty list that will hold the inverse values
    for key in f: #goes through each key in f
        for x in a: #goes through each element in the codomain
            if f[key] == x: #creates condition that the value in the dictionary must equal the element in the codomain
                inverse.append(key) #adds key to inverse list
    return inverse #returns inverse list

