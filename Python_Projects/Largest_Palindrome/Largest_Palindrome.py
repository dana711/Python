palindromes = []
for x in range(100,1000):
    for i in range(100,1000):
        num = str(i * x).split()[0]
        if (x < 1000) and (i < 1000):
            if (num[::-1] == num):
                palindromes.append(i * x)
            else:
                continue
        else:
            continue
print(max(palindromes))
