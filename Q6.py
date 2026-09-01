n = int(input("Enter the number of elements: "))

hash = [[], [], [], [], [], [], [], [], [], []]

def binarySearch(arr, num):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2

        if arr[mid] < num:
            low = mid + 1
        else:
            high = mid
    return low


for i in range(n):
    num = int(input("Enter a number: "))
    index = num % 10
    position = binarySearch(hash[index], num)
    hash[index].insert(position , num)

print("Hash table = ")
for i in range(10):
    print(i, ":", hash[i])
