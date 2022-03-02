list1 = ['False', 'False','False','True','True']
#Find the boundary where the boundary is the first true element index

from typing import List

def find_boundary(arr: List[bool]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    l = 0
    r = len(arr) -1
    boundary_index =-1
    while l<=r:
        mid= (r+l)//2
        
        if arr[mid]:
            r = mid-1
            boundary_index = mid
        else:
            l = mid+1
    return boundary_index

# To find the last false That is left of bondary, put boundary_index = mid in else statement
