def diffSequence(seq):  # creates diffSequence with seq as input
    diffList = []  # creates empty list
    index = 1  # sets index to 1
    while (index < len(seq)):  # goes through each element in seq
        diffList.append(seq[index] - seq[index - 1])  # adds the difference of each element and the element before
        index += 1  # incremements the index
    return diffList  # returns the list of differences

a = [1,2,3,4,5,6,7]
print(diffSequence(a))


def constSequence(seq):  # creates cosntSequence with seq as input
    diffList1 = []  # creates empty list
    diffList2 = []  # creates empty list
    index1 = 1  # sets index to 1
    index2 = 1  # sets index to 1
    constList = []  # creates empty list
    while (index1 < len(seq)):  # goes through each elements in seq
        diffList1.append(seq[index1] - seq[index1 - 1])  # adds the difference of each element and the element before
        index1 += 1  # increments the index
    while (index2 < len(diffList1)):  # goes through each element in diffList1
        diffList2.append(
            diffList1[index2] - diffList1[index2 - 1])  # adds the difference of each element and the element before
        index2 += 1  # increments the index
    for element in diffList2:  # goes through each element in diffList 2
        if element not in constList:  # creates condition that the element must be unique
            constList.append(element)  # adds unique element to constList
    if (len(constList) == 1):  # sets condition that constList size must be 1
        return True  # returns true if condition holds true
    return False  # returns false otherwise

print(constSequence(a))
