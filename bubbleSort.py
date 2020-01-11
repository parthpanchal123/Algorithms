

def bubbleSort(mylist,length):
    for i in range(length-1):    # outer loop running length-1 times 
        for j in range(length-i-1):   # we could do simply length-1 here, but length-i-1 helps to  minimize the comparisons since at the end of each pass the greatest element will be at the last index , so we need not compare the element at last index with the element at the second last index in list . Therefore at each pass ie for pass = i , we save  length-i-1 comparisons
            if mylist[j] > mylist[j+1]:    # comparing the adjacent elements
                mylist[j],mylist[j+1] = mylist[j+1],mylist[j]

    return mylist


if __name__ == "__main__":
    mylist = list(map(int,input("Enter a list of numbers to sort seperated by space : ").split(" ")))    # getting the input list and storing it in mylist
    print(bubbleSort(mylist,len(mylist)))  # passing the mylist and its length to  bubbleSort function and printing the sorted list



'''An example
i= 0 
1st pass
4 3 2 1 
3 4 2 1 
3 2 4 1
3 2 1 4

i= 1
2nd pass
2 3 1 4 
2 1 3 4
2 1 3 4

i=2
3rd pass    Because of n-i-1 , this will run only once 
1 2 3 4   
'''
