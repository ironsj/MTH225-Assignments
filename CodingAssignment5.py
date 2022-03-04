def bitToSet(B): #creates bitToSet function with input B
    b = [int(x) for x in str(B)] #converts bit string into a list
    subset = [] #creates an empty list to be returned
    index = 0 #sets index at 0
    while index < len(b): #creates condition that the index must be less than the length of the list
            index = b.index(1, index) #sets index equal to the index of the first 1 after the value index is set to
            subset.append(index+1) #adds the index of the 1 (adds 1 so that index 0 is the '1' position for example)
            index += 1 #increments the index
    return subset #returns the subset of positions of 1 in the bit string

def latticeToSet(P): #creates latticeToSet function with input P
    subset = [] #creates an empty list to be returned
    index = 0 #sets index to 0
    while index < len(P): #creates condition that index must be less than the length of the list
        index = P.index('up', index) #sets index equal to the index of the first 'up' after the value index is set to
        subset.append(index+1) #adds the index of the 'up' (adds 1 for same reason as function above)
        index +=1 #increments the index
    return subset #returns the subset of positions of 'up' in the lattice path

def bitToLattice(B): #creates bitToLattice function with input B
    b = [int(x) for x in str(B)] #converts bit string to list
    set = ['up' if x == 1 else 'right' for x in b] #changes 1 to 'up' if an element is 1 and 'right' otherwise
    return set #returns the lattice path

A = "0101111"
print(bitToSet(A))