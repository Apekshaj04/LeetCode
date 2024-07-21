H=[0]*50
size=-1 
def swap(i,j):
    H[i],H[j]=H[j],H[i]
    
def parent(i):
    return (i-1)//2 

def leftChild(i):
    return (2*i)+1

def rightChild(i):
    return (2*i)+2

def shiftUp(i):
    while i>0 and H[parent(i)]<H[i]:
        swap(parent(i),i)
        i=parent(i)
        
def insert(p):
    global size 
    size+=1 
    H[size]=p 
    shiftUp(size)
    

def shiftDown(i):
    maxIndex=i 
    l=leftChild(i)
    if l<=size and H[l]>H[maxIndex]:
        maxIndex=l 
    r=rightChild(i)
    if r<=size and H[r]>H[maxIndex]:
        maxIndex=r 
    if i!=maxIndex:
        swap(i,maxIndex)
        shiftDown(maxIndex)
    
def extractMax():
    global size 
    result=H[0]
    H[0]=H[size]
    size-=1 
    shiftDown(0)
    return result

def getMax():
    return H[0]

def changePriority(i,p):
    oldp=H[i]
    H[i]=p 
    if p>oldp:
        shiftUp(i)
    else:
        shiftDown(i)
    
def delete(i):
    H[i]=getMax()+1 
    shiftUp(i)
    extractMax()
    

# Insert elements into the priority queue
insert(45)
insert(20)
insert(14)
insert(12)
insert(31)
insert(7)
insert(11)
insert(13)
insert(7)

# Display the priority queue before extracting max
print("Priority Queue:", end=" ")
for i in range(size + 1):
    print(H[i], end=" ")
print()

# Display the node with maximum priority
print("Node with maximum priority:", extractMax())

# Display the priority queue after extracting max
print("Priority queue after extracting maximum:", end=" ")
for i in range(size + 1):
    print(H[i], end=" ")
print()

# Change the priority of element at index 2 to 49
changePriority(2, 49)
print("Priority queue after priority change:", end=" ")
for i in range(size + 1):
    print(H[i], end=" ")
print()

# Remove element at index 3
remove(3)
print("Priority queue after removing the element:", end=" ")
for i in range(size + 1):
    print(H[i], end=" ")
print()
    

