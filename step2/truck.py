#truck

list= list(map(int, input().split(" ")))
result = 'NO CRASH'

for i in range(len(list)):
  if (list[i] < 168):
    result = f'CRASH {list[i]}'
    break

print(result)

