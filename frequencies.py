"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    listOfItm = []
    listOfItmOccurance = []
    
    for i in items:
        itm = str(i) # item of time string.
        listOfItm.append(itm)
    listOfItmChecked = []
    for x in listOfItm:
        if(x not in listOfItmChecked):
            listOfItmChecked.append(x)
            listOfItmOccurance.append(listOfItm.count(x))    
        
    frequencies2 = dict(zip(listOfItmChecked, listOfItmOccurance))
    # Your code goes here
    return frequencies2
    # the key must be the item converted to a string
    #The value must be a positive integer counting the number of times the item represented by the key occurs in items

    #For example, frequencies(['a', 'a', 'b', 'b', 'b', 'c']) must return the following dictionary: { 'a': 2, 'b': 3, 'c': 1 }

    #For example, frequencies([100, 'Hello', '100', '100', 100]) must return the following dictionary: { '100': 4, 'Hello': 1 }
    # for every item in ITEMS you convert into string, if count is zero then add to list,
    # if item is the first element i add to dictionary,
    # for every next item i have to check with my list whether it exist, if exist then dont add to list and add count.
    