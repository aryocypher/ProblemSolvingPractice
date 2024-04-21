from typing import List

def selectionSort(arr: List[int]) -> None: 
    # Write your code here
    for i in range(len(arr)):
        smallest=arr[i]
        smallestIndex=i
        for j in range(i+1,len(arr)):
            if arr[j]<smallest:
                smallestIndex=j
                smallest=arr[j]
        
        arr[i],arr[smallestIndex]=arr[smallestIndex],arr[i]
    
