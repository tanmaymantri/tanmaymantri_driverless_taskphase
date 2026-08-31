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

words = input("Enter string (use space): ").split()
obj = SelectionSort()
result = obj.sort(words)
print("Sorted string: ", result)
