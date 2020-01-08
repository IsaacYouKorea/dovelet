a = int(input())
b = int(input())
temp = b
first = temp % 10
temp = int(temp / 10)
second = temp % 10
temp = int(temp / 10)
third = temp % 10
temp = int(temp / 10)

print("%d\n%d\n%d\n%d" % (a * first, a * second, a * third, a * b))