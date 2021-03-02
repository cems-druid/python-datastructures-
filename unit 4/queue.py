#queue creation, dequeue, enqueue, front, isEmpty -> O(1)

class Queue:
    def __init__(self):
        self.items = []
        self.frontIdx = 0

    def __compress(self):
        newlist = []
        for i in range(self.frontIdx,len(self.items)):
            newlist.append(self.items[i])

        self.items = newlist
        self.frontIdx = 0

    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty queue")

        if self.frontIdx * 2 > len(self.items):
            self.__compress() #if list is longer than it is needed, shorten it.

        item = self.items[self.frontIdx]
        self.frontIdx += 1 #remove (dequeue) the item
        return item

    def enqueue(self, item):
        self.items.append(item)

    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to access front of empty queue")

        return self.items[self.frontIdx]


    def isEmpty(self):
        return self.frontIdx == len(self.items) 
        #it is true if only both are 0

    
def main():
    q = Queue()
    lst = list(range(10))
    lst2 = []

    for k in lst:
        q.enqueue(k) # front[0,1,2,3,4,5,6,7,8,9]

    
    if q.front() == 0:
        print("Test 1 passed")

    else:
        print("Test 1 failed")

    while not q.isEmpty():
        lst2.append(q.dequeue()) #lst2 -> front[0,1,2,3,4,5,6,7,8,9]

    if lst2 != lst:
        print("Test 2 failed")
    else:
        print("Test 2 passed")

    #Resetting

    for k in lst:
        q.enqueue(k)

    lst2 = []

    while not q.isEmpty():
        lst2.append(q.dequeue())

    if lst2 != lst:
        print("Test 3 failed")
    else:
        print("Test 3 passed")

    try:
        q.dequeue()
        print("Test 4 failed")

    except RuntimeError:
        print("Test 4 passed")
    except:
        print("Test 4 failed")

    try:
        q.front()
        print("Test 5 failed")
    except RuntimeError:
        print("Test 5 passed")
    except:
        print("Test 5 failed")
    
if __name__ == "__main__":
    main()
