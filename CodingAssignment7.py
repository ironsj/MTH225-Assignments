def recursiveSequence(c1, c2, a0, a1): #creates recursiveSequence function with inputs c1, c2, a0, a1
    recursionList = [a0, a1] #creates list with a0 and a1 as first elements
    index = 2 #sets index to 2
    while (index <= 14): #makes it so list only contains first 15 terms
        recursionList.append(c1*recursionList[index-1] + c2*recursionList[index-2]) #adds next term to list based on recursive equation
        index += 1 #increments the index
    return recursionList #returns the list containing the sequence


def arithmeticSequence(initial, difference, last_index): #creates arithmeticSequence function with initial, difference and last_index as inputs
    arithmeticList = [initial] #creates list containg first term in sequence
    index = 0 #sets index to 0
    while(index + 1 <= last_index): #makes it so the list contains terms up until the last one in the index
        arithmeticList.append(arithmeticList[index] + difference) #adds next term by taking last term in list and adding the difference
        index += 1 #increments the index
    return arithmeticList #returns the list containing the sequence

def geometricSequence(initial, ratio, last_index): #creates geometricSequence function with initial, ratio and last_index as inputs
    geometricList = [initial] #creates list containing first term in sequence
    index = 0 #sets index to 0
    while (index + 1 <= last_index): #makes it so the list contains terms up until the last one in the index
        geometricList.append(geometricList[index] * ratio) #adds next term by taking last term in list and multiplying by the ratio
        index += 1 #increments the index
    return geometricList #returns the list containing the sequence