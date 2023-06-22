a= [-4, 2, 3]

def sortedSquaredArray(array):
    # Write your code here.
    result = []
    for i in array:
        result.append(i*i)

    result.sort()

    return result

# o(nlog(n))
print(sortedSquaredArray(a))