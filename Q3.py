class SelectionSort:
    def sort(self, words):
        n = len(words)

        for i in range(n):
            index = i
            for j in range(i+1, n):
                if words[j] < words[index]:
                    index = j
            new = words[i]
            words[i] = words[index]
            words[index] = new
        return words

class BinarySearch:
    def search(self, words, target):
        low = 0
        high = len(words) - 1
        while low <= high:
            mid = (low + high) // 2
            if words[mid] == target:
                return True
            elif words[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

words = input("Enter words: ").split()
obj = SelectionSort()
words = obj.sort(words)
print("Sorted words:", words)

target = input("Enter word to search: ")
search_object = BinarySearch()
result = search_object.search(words, target)
if result:
    print("String found")
else:
    print("String not found")
