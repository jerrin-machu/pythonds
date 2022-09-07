
 # 6,5,7,9,4,0,2
def arraySum(arr,target):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target :
                return [ arr[i], arr[j]]


    return []

arr = [6,5,7,9,4,0,2]

target = 10

result = arraySum(arr,target)

print(result)
