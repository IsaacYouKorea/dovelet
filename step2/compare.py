#http://59.23.150.58/30stair/compare/compare.php?pname=compare

a, b = map(int, input().split(" "))

if a > b:
  print(">")
elif a == b:
  print("=")
else:
  print("<")