
def swap(mylist, i, j):
    '''
        function for swapping mylist[i] and mylist [j]
    '''
    t = mylist[i]
    mylist[i] = mylist[j]
    mylist[j] = t


def partition(mylist, left, right):
    '''
           this function returns the index of the latest least number which is less than or equal to the pivot . 
    '''
    pivot = mylist[right]   # Initially we assume the last elemeny to be the pivot
    i = left-1

    for j in range(left, right):   # do not include the index of pivot
        if mylist[j] <= pivot:
            i += 1
            swap(mylist, i, j)

    swap(mylist, i+1, right)
    return i+1


def quickSort(mylist, left, right):
    if left < right:
        p_index = partition(mylist, left, right)
        # only go upto p_index -1 here , as the element at index p_index will be already at its correct position
        quickSort(mylist, left, p_index-1)
        # the same above rule applies here
        quickSort(mylist, p_index+1, right)


if __name__ == "__main__":
    mylist = list(map(int, input("Enter a list of numbers to sort seperated by space : ").split(
        " ")))    # getting the input list and storing it in mylist
    # passing the mylist and its length to selectionSort function and printing the sorted list
    quickSort(mylist, 0, len(mylist)-1)
    print("The sorted list is " + str(mylist))
