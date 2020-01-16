#grp
n, k = map(int, input().split(" "))
count = 0
a = (k * (1 + k) / 2)

for i in range(n - k):
  if (int(a + (k * (i))) % 15 == 0):
    count = count + 1
  
print(count)

