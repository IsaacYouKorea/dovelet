#coci_tablica

a, b = map(int, input().split(" "))
c, d = map(int, input().split(" "))

numberList = []


# a b
# c d

# c a
# d b

# d c
# b a

# b d
# a c

numberList.append(a/c + b/d)
numberList.append(c/d + a/b)
numberList.append(d/b + c/a)
numberList.append(b/a + d/c)

numberList.index(max(numberList))
print(numberList.index(max(numberList)))
