n = int(input("Enter the size of list: "))
list = []
for i in range(n):
    word = input("Enter word: ")
    list.append(word)

count = {}

for word in list:
    for char in word:
        if char in count:
            count[char] +=1
        else:
            count[char] =1
print(count)
