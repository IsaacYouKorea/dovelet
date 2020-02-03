#seq
a, b = map(int, input().split(" "))

big = a if a > b else b
small = b if a > b else a

strResult = ""
for i in range(big - small + 1):
  strResult += str(i + small)
  strResult += " "

print(strResult)