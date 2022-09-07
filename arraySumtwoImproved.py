# 6,5,7,9,4,0,2

def findSumArrayTwo(arr, target):
    numset = set()
    for i in range(0,len(arr)):
        num = arr[i]
        diff = target - num
        if diff in numset:
            return [ num, diff]
        else:
            numset.add(num)
    return []

arr = [ 6,5,7,9,4,0,2]
target = 10

result = findSumArrayTwo(arr,target)
print(result)