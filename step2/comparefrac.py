#http://59.23.150.58/30stair/comparefrac/comparefrac.php?pname=comparefrac
#comparefrac

a, b, c, d = map(int, input().split(" "))

value1 = a / b
value2 = c / d

if value1 > value2:
  print(1)
elif value1 == value2:
  print(0)
else:
  print(-1)