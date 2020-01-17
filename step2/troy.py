#troy
troy = int(input())
haveLumber = int(input())
needLumberPerTroy = 1000


if haveLumber >= troy * needLumberPerTroy:
  print('O')
else:
  print('X')