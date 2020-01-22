# ATM

a, b = input().split(" ")
a = int(a)
b = float(b)

if(a % 5 == 0 and (a + 0.5) <= b):
  print('%.2f' % (b - (a + 0.5)))
  
else:
  print('%.2f' % b)