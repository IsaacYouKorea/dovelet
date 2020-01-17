#-*- coding:utf-8 -*-

y, m, d = map(int, input().split(" "))

a = y + m + d
print(a)
if (a % 10 == 0):
  print('운수대통!')
else:
  print('노력하세요!')

