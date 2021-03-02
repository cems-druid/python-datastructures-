import random

def partition(seq, start, stop):
    pivotIndex = start
    pivot = seq[pivotIndex]
    i = start +1
    j = stop -1

    while i <= j:
        #Smaller than the pivot value
        while i <= j and not pivot < seq[i]:
             i += 1
        #Bigger than the pivot value
        while i <= j and pivot < seq[i]:
            j -= 1

        if i<j:
            temp = seq[i]
            seq[i] = seq[j]
            seq[j] = temp
            i += 1
            j -= 1

    seq[pivotIndex] = seq[j]
    seq[j] = pivot
    return j


def quicksortRecursively(seq, start, stop):
    if start >= stop - 1:
        return 
    
    pivotIndex = partition(seq, start, stop)

    quicksortRecursively(seq, start, pivotIndex)
    quicksortRecursively(seq, pivotIndex+1, stop)

def quicksort(seq):
    for i in range(len(seq)):
        j = random.randint(0, len(seq)-1)
        tmp = seq[i]
        seq[i] = seq[j]
        seq[j] = tmp

    quicksortRecursively(seq, 0, len(seq))

