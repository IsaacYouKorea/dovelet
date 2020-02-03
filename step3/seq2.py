#seq2

a = int(input())

for i in range(1, a + 1, 1):
  print("%d..%d %d" %(1, i, sum(range(1, i + 1, 1))))