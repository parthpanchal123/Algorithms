
def insertion_sort(arr):
    for i in range(1, len(arr)):
        hole = i
        value = arr[i]
        while(hole > 0 and arr[hole - 1] > value):
            arr[hole] = arr[hole-1]
            hole -= 1
        arr[hole] = value
    return arr


if __name__ == "__main__":
    print('Enter elements to sort')
    my_arr = list(map(int, input().split(" ")))
    print(insertion_sort(my_arr))



