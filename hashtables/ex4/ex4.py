def has_negatives(a):
    # Your code here
    #sort array from low to high
    sorted_array = sorted(a)
    #initialize variables
    cache = {}
    result = []
    num = 0
    #put array in a dictionary
    for i in range(len(a)):
        cache[a[i]] = i
    #checking array starting from lowest value and stopping before 0
    while sorted_array[num] < 0:
        positive_number = sorted_array[num] * -1
        #if the positive version of the number is in the dictionary
        if positive_number in cache:
            #add to front of result array
            result.insert(0, positive_number)
        num +=1
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
