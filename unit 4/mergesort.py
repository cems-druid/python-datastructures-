def merge(seq, start, mid, stop):
    lst =[]
    i = start 
    j = mid

    while i<mid and j<stop:
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i += 1

        else:
            lst.append(seq[j])
            j += 1

        
    while i<mid:
        lst.append(seq[i])
        i += 1

    for i in range(len(lst)):
        seq[start+i] = lst[i]

    
def mergeSortRecursively(seq, start, stop):
    if start >= stop-1:
        return 

    mid = (start + stop)/2

    mergeSortRecursively(seq,start,mid)
    mergeSortRecursively(seq, mid, stop)
    merge(seq, start, mid, stop)


#Merge sort's complexity time is = merging --> O(n) splitting the list --> O(log n) ==> O(n log n)

def mergeSort(seq):
    mergeSortRecursively(seq, 0, len(seq))
