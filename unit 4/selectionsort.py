def select(seq, start):
    minIndex = start
    
    for j in range(start+1, len(seq)):
        if seq[minIndex] > seq[j]:
            minIndex = j

    return minIndex

def selectionSort(seq):
    for i in range(len(seq)-1):
        minIndex = select(seq, i)
        tmp = seq[i]
        seq[i] = seq[minIndex]
        seq[minIndex] = tmp


def main():
    list1 = [5,8,2,6,9,1,0,7]
    print(list1)
    selectionSort(list1)
    print(list1)
  
    #Since there are two loops the complexity is O(n^2)

if __name__ == "__main__":
    main()