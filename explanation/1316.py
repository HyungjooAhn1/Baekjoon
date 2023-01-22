n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    alphabet = []
    for i in range(len(word)):
        if i == 0:
            alphabet.append(word[i])
        else:
            if word[i] == alphabet[-1]:
                continue
            else:
                alphabet.append(word[i])
    for i in range(len(alphabet)):
        if alphabet[i] in alphabet[i+1:]:
            break
    else:
        cnt += 1
print(cnt)