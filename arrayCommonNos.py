# 6,1,6,8,10,5,4,5,3,5,6,9,6,5

def commonElements(arr, target):
    j = len(arr)-1
    for i in range(0,len(arr)):
        if arr[j] == target:
            j=j-1
        if arr[i] == target:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            j=j-1

        if i == j:
            break
    return arr

arr = [6,1,6,8,10,5,4,5,3,5,6,9,6,5]
target = 6

result  = commonElements(arr,target)

print(result)
