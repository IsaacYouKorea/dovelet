#div_mul

m, n = map(int, input().split(" "))

if(n == 0):
  print(f'{m} | {n}')
elif(m == 0):
  print(f'{m} !| {n}')
else:
  if(n % m == 0):
    print(f'{m} | {n}')
  else:
    print(f'{m} !| {n}')