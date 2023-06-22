a = [-4, -3, 1, 2, 3, 5]

def sortedSquaredArray(array):
    # Write your code here.
    result = [0] * len(array)

    print(result)

    start = 0

    end = len(array) - 1

    while start <= end:
        if abs(array[start]) >= abs(array[end]):
            result.append(array[start] * array[start])
            start = start + 1

        else:
            result.append(array[end] * array[end])
            end = end - 1

    return result[::-1]


# o(nlog(n))
print(sortedSquaredArray(a))
