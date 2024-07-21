def getParent(x):  # get parent node , if exits else -1
    return (x - 1) // 2


def leftChild(x):  # get left child if exists, else -1
    return (2 * x + 1) if (2 * x + 1) < curr_size else -1


def rightChild(x):  # get right child if exits, else -1
    return (2 * x + 2) if (2 * x + 2) < curr_size else -1

#Function to maintain the min heap property of heap.
def heapify():
    
    curr_ind = curr_size - 1
    while getParent(curr_ind) != -1 and heap[getParent(curr_ind)] > heap[curr_ind]:
        heap[curr_ind], heap[getParent(curr_ind)]=heap[getParent(curr_ind)],heap[curr_ind]
        curr_ind = getParent(curr_ind)

    return


def heapifyDown(x):
    
    # if the removed index was leaf.
    if x >= curr_size:  
        return
    
    if getParent(x) != -1 and heap[x] < heap[getParent(x)]:
        heap[x], heap[getParent(x)] = heap[getParent(x)], heap[x]
        heapifyDown(getParent(x))
        
    if leftChild(x)==-1 or (leftChild(x)!=-1 and heap[x]<heap[leftChild(x)]):
        if rightChild(x)==-1 or (rightChild(x)!=-1 and heap[x]<heap[rightChild(x)]):
            return 
    
    #swapping with left child and calling function recursively for left child. 
    if rightChild(x)==-1:
        heap[x], heap[leftChild(x)] = heap[leftChild(x)], heap[x]
        heapifyDown(leftChild(x))
        
    #swapping with right child and calling function recursively for right child.
    elif leftChild(x) == -1:
        heap[x], heap[rightChild(x)] = heap[rightChild(x)], heap[x]
        heapifyDown(rightChild(x))
        
    #swapping with the minimum of the two childs.    
    else:
        if heap[rightChild(x)]<heap[leftChild(x)]:
            heap[x], heap[rightChild(x)] = heap[rightChild(x)], heap[x]
            heapifyDown(rightChild(x))
        else:
            heap[x], heap[leftChild(x)] = heap[leftChild(x)], heap[x]
            heapifyDown(leftChild(x))
    return


#Function to insert a value in Heap.
def insertKey (x):
    
    global curr_size
     #inserting value at current available index.
    heap[curr_size] = x 
    curr_size += 1
    #calling heapify function to maintain heap property.
    heapify()  

#Function to delete a key at ith index.
def deleteKey (i):
    
    global curr_size

    if i >= curr_size: 
        return
    #storing value of leaf node at ith index.
    heap[i] = heap[curr_size - 1]
    heap[curr_size - 1] = 0
    curr_size -= 1  

     #calling heapify function to maintain heap property from index i.
    heapifyDown(i) 

#Function to extract minimum value in heap and then to store 
#next minimum value at first index.
def extractMin ():
    
    if curr_size == 0:  
        return -1

    #storing value at first index in a variable.
    val = heap[0] 
    #deleting the value at first index.
    deleteKey(0)   
    return val   

