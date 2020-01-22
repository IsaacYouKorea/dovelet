#punch_game

a, b, c, d, e = map(int, input().split(" "))

damage = a * 10 + b * 15 + c * 20 + d * 25 + e * 30
time = a + b + c + d + e

if(time <= 10):
  if(damage >= 100):
    print('you win')
  else:
    print('game over')
else:
  print('time out')