def count_vowels(words):
    vowels = "aeiouAEIOU"
    result = {}

    for word in words:
        count = 0
        for ch in word:
            if ch in vowels:
                count += 1
        result[word] = count

    return result
words = input("Enter words separated by space: ").split()
output = count_vowels(words)
print(output)
