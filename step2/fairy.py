#fairy

year = int(input())
if(year < 2000):
  print('X')

else:
  num = year - 2000
  print("O" if num % 8 == 0 else "X")