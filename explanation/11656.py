s = input()
words = []
for i in range(len(s)):
    words.append(s[i:])
words.sort()
for word in words:
    print(word)