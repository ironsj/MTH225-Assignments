def inclusionExclusion3(S, T, U): #creates inclusion-exclusion function with lists S, T, and U as inputs
    cardinality = 0 #sets the cardinality of the union of sets to 0
    allSets = intersect(U, intersect(S, T)) #creates a list that is the intersection of the inputs
    for s in S: #loops through each element in S
        cardinality += 1 #adds 1 to the cardinality for each element in S
    for t in T: # loops through each element in T
        cardinality += 1 #adds 1 to the cardinality for each element in T
    for u in U: #loops through each element in U
        cardinality += 1 #adds 1 for each element in U
    for element in intersect(S, T): #loops through each element in the intersection of S and T
        cardinality -=1 #subtracts 1 from the cardinality for each element in S and T
    for element in intersect(S, U): #loops through each element in the intersection of S and U
        cardinality -=1 #subtracts 1 from the cardinality for each element in S and U
    for element in intersect(U, T):#loops through each element in the intersection of U and T
        cardinality -= 1 #subtracts 1 from the cardinality for each element in U and T
    for element in allSets: #loops through each element in the intersection of each set
        cardinality += 1 #adds 1 to the cardinality for each element in the intersection of each set
    return cardinality #returns the cardinality

def additive3(S, T, U): #creates the additive3 function with inputs S, T, and U
    if(len(intersect(S, T)) != 0): #creates a condition for if the cardinality of the intersection of S and T does not equal 0
        return False #returns false if the condition holds true
    if(len(intersect(S, U)) != 0): #creates a condition for if the cardinality of the intersection of S and U does not equal 0
        return False #returns false if the condition holds true
    if(len(intersect(T, U)) != 0): #creates a condition for if the cardinality of the intersection of U and T does not equal 0
        return False #returns false if the condition holds true
    return len(S) + len(T) + len(U) #returns the cardinality of each set


#below is the intersection function from coding assignment 2 that will help the functions above
def intersect(A, B): #creates intersect funtion with lists A & B as arguments
    temp_list = [] #creates temporary list to be used in the function
    intersect_list = [] #creates list that will be intersection of A & B
    for element in A: #goes through elements of A
        if element in B: #creates a condition that makes it so element must also be in B
            temp_list.append(element) #adds elements to temporary list
    for element in temp_list: #goes through elements in the temporary list
        if element not in intersect_list: #creates a condition for anything not in list already
            intersect_list.append(element) #adds elements to final list
            intersect_list.sort() #sorts list in ascending order
    return intersect_list #returns the final list





