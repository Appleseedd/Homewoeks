def summs(n):
    for i in range(1, n):
        for j in range(1, i):
            if n % (i + j) == 0:
                print(i, j)



n = int(input())
summs(n)
