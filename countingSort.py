

def insertion_sort(arr, k):
    # initializing the count list to track no of occurence of each int i in the input list . (max(arr)+1) if the max element is 5 , then count = [0,0,0,0,0,0]
    count = [0] * (max(arr)+1)
    # the final output arrayto store the sorted integers . it will be of the same length as of the input list
    output = [0] * k
    # here arr is the list of numbers and k is the length of the list .
    # this is the list for storing the occurences of each integer in the given list.
    for i in range(k):
        # for each integer in the given list , we place the times of occurence of i in the count list at index denoted by the integer i itself
        count[arr[i]] = arr.count(arr[i])

    for i in range(1, len(count)):
        # at each index count[i] placing the sum of current value and the value at previous index
        count[i] += count[i-1]

    for i in range(len(arr)-1, -1, -1):   # this will start counting from reverse
        target = arr[i]     # fetch the last number in the input list
        # find the target numbers index int the count list
        index = count[target] - 1
        # place the target integer at the appropriate index
        output[index] = target
        count[target] -= 1  # decrent the count value in thr count list

    return output    # return the sorted result


if __name__ == "__main__":
    print('Enter elements to sort')
    my_arr = list(map(int, input().split(" ")))
    print(insertion_sort(my_arr, len(my_arr)))
