def trueListFunc(B): #creates function trueListFunc
    trueList = {} #creates empty dictionary
    trueList[0] = B #sets the first key value in the dictionary equal to B
    n = 1 #sets n equal to 1
    while n < 21: #creates 20 other keys in the dictionary
        trueList[n] = None #sets the rest of they keys equal to None
        n += 1 #increments n
    for key in trueList: #goes through each key in trueList
        if(key < 20): #makes it so it stops at the second to last key (19)
            if trueList[key] == True: #sets condition that the key must be true
                trueList[key + 1] = True #if condition is met then the next key is True
    return trueList #returns trueList

B = True;
print(trueListFunc(B))
#if B is false then the rest of the keys do not get filled since we only know what happens if B is true

'''This is a great example of a induction problem. We start with our base case, which is the first key equals True. Then,
we assume that if trueList[k] = True, then trueList[k+1] = True. Then we show that when trueList[k+1] = True,
then trueList[k+2] == True. We show this by calling the function in a print statement.'''

