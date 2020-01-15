#flr
f = int(input())

i = 0
while True:
  value = pow(2, i) - 1
  if value >= f :
    print(i)
    break
  i = i + 1
