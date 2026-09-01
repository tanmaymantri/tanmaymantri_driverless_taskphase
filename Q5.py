n = int(input("Enter the number of elements: "))
hash = [[], [], [], [], [], [], [], [], [], []]
for i in range(n):
    num = int(input("Enter the element: "))
    index = num % 10
    hash[index].append(num)

print("Hash table = ")
for i in range(10):
    print(i, ":", hash[i])
