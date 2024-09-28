def closest_to_sum(arr):
    arr.sort()
    left=0
    right=len(arr)-1
    closest_sum=float('inf') 
    while left<right:
        current_sum=arr[left]+arr[right]
        if abs(current_sum)<abs(closest_sum):
            closest_sum=current_sum
        if current_sum<0:
            left+=1
        else:
            right-=1
    return closest_sum
arr=[1,5,-2,3,-1,7,-4]
print(closest_to_sum)