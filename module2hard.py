
def summs(result, *dig):
    res = []
    for i in dig:
        for j in dig:
            if i + j == result and (i, j) not in res and (j, i) not in res:
                res.append((i, j))
    return res


print(summs(3, *range(3)))
print(summs(4, *range(4)))
print(summs(5, *range(5)))
print(summs(6, *range(6)))
print(summs(7, *range(7)))
print(summs(8, *range(8)))
print(summs(9, *range(9)))
print(summs(10, *range(10)))
print(summs(11, *range(11)))
print(summs(12, *range(12)))
print(summs(13, *range(13)))
print(summs(14, *range(14)))
print(summs(15, *range(15)))
print(summs(16, *range(16)))
print(summs(17, *range(17)))
print(summs(18, *range(18)))
print(summs(19, *range(19)))
print(summs(20, *range(20)))

#import itertools as it
#
#
#a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
#b = 3
#for i in range(len(a)):
#    comb = it.combinations(a, 2)
#    result = [i for i in comb if sum(i) == b]
#    b += 1
#
#    print(result)
