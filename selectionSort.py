
def selectionSort(mylist,length):
    for i in range(length-1):                # the outer loop that will run length-1 times . For eg 4,3,2,1 it will run for 4,3,2 ie 3 times and not for last element 1 because the last element would be already sorted
        j = i+1                  # setting the variable j to 1 index higher than i for comparison
        k = i                  # k is a variable which will store the index of smallest number in the list . Initially , we assume the first element in list to be the smallest. Hence its index will be 0 ie k=0
        for j in range(j,length):  # the inner loop that will tarverse the inner array starting from j till the last element index
            if(mylist[j] < mylist[k]):     # if the element at index j is smaller than our least assumed element at index k , then the next step
                k = j      # we assign the variable k which points to the smallest element's index to the element at index j
        # at the end of each pass , we will have the index of the smallest element stored in variable k , so now we'll just replace both elements , ie our least assumed element at index i and the element at index k            
        t=mylist[k]
        mylist[k] = mylist[i]
        mylist[i] = t
    
    return (mylist)

if __name__ == "__main__":
    mylist = list(map(int,input("Enter a list of numbers to sort seperated by space : ").split(" ")))    # getting the input list and storing it in mylist
    print(selectionSort(mylist,len(mylist)))  # passing the mylist and its length to selectionSort function and printing the sorted list








