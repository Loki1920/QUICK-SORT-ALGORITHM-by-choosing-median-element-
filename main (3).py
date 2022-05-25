#QUICK SORT ALGORITHM by choosing median element 
#function to find correct position of pivot

import statistics 
def pivot_place(list1,first,last):
  low = list1[first]
  high = list1[last]
  mid = (first+last) // 2
  pivot_val = statistics.median([low,list1[mid],high])
  if pivot_val == low :
    pindex = first
  elif pivot_val == high:
    pindex = last
  else:
    pindex = mid 

  list1[last],list1[pindex] = list1[pindex],list1[last]
  pivot = list1[last]
  left = first 
  right = last - 1
  
  while True:
    while left <= right and list1[left] <= pivot:
      left += 1
    while left <= right and list1[right] >= pivot:
      right = right -1 
    if right < left:
      break
    else:
      list1[left],list1[right] = list1[right],list1[left]
  list1[last],list1[left] = list1[left],list1[last]
  return left

def Quicksort(list1,first,last):
  if first < last :
    p = pivot_place(list1,first,last)
    Quicksort(list1,first,p-1)
    Quicksort(list1,p+1,last)

list1 = [56,26,93,17,3,44]
n = len(list1)
Quicksort(list1,0,n-1)
print(list1)

