def intersection(arrays):
    # Your code here
    #dictionary to hold all values in all arrays
    intersection_junction = {}
    #empty array to hold results
    results = []
    #using the number of arrays to check if we have the right number of elements
    number_of_arrays = len(arrays)

    #load intersection junction with values in array and count each occurance
    for array in arrays:
        for i in array:
            if i not in intersection_junction:
                intersection_junction[i] = 1
            else:
                intersection_junction[i] += 1
        for i in intersection_junction:
            #add all values that have appeared in all arrays to results list
            if intersection_junction[i] == number_of_arrays:
                results.append(i)
    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
