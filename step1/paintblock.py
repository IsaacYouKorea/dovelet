#paintblock.py
w, h, d = map(int, input().split(" "))
print(((h - 2) + (w - 2) + (d - 2)) * 4)