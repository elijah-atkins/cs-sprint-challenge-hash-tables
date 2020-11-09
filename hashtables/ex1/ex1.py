def get_indices_of_item_weights(weights, length, limit):
    #create object to hold hash
    hashtable = {}
    #load dictionary with objects in the weights array
    for i in range(length):
        hashtable[weights[i]] = i

    # we can then loop through the dictionary to see if we have a matching number 
    for index, weight in enumerate(weights):
        #find the target weight of the complimentry item
        target_weight = limit - weight
        #if an object with the target weight exist in hash table
        if target_weight in hashtable:
            #get the index of the item with the target weight
            i = hashtable[target_weight]
            #sort results low to high
            return (index, i) if index > i else (i, index)
    return None
