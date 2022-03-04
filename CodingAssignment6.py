def listPairs(A): #creates listPairs function with input A
    card2 = [] #creates list that will contain all subsets of cardinality 2
    n = len(A) #creates variable that equals the length of the list A
    subset = [] #creates a list that will hold each individual subset
    for i in range(0, n): #creates a loop that will go through each element in A
        for j in range(i + 1, n): #creates a loop that will go through every element after the first element
            subset = [A[i], A[j]] #adds the the element in A at index i and j to subset
            card2.append(subset) #adds subset to card2
    return card2 #returns card2

def listTriples(A): #creates listTriples function with input A
    card3 = [] #creates list that will contain all subsets of cardinality 3
    n = len(A) #creates variable that equals the length of list A
    subset = [] #creates a list that will hold each individual subset
    for i in range(0, n): #creates a loop that will go through each each element in A
        for j in range(i + 1, n): #creates a loop that will go through every element after the first element
            for k in range(j+1, n): #creates a loop that will go through every element after the second element
                subset = [A[i], A[j], A[k]] #adds the element in A at index i, j and k to subset
                card3.append(subset) #adds subset to card3
    return card3 #returns card 3