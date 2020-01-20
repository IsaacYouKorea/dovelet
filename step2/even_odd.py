#even_odd

a, b = map(int, input().split(" "))

def oddeven(num) :
  return 'even' if num % 2 == 0 else 'odd'


print(f'{oddeven(a)}+{oddeven(b)}={oddeven(a+b)}')
print(f'{oddeven(a)}*{oddeven(b)}={oddeven(a*b)}')