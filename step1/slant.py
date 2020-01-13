#slant
x1, y1 = map(int, input().split(" "))
x2, y2 = map(int, input().split(" "))

ratio = (y2 - y1) / (x2 - x1)

print(int(ratio), int(y1 - (x1 * ratio)))