#coci_spa
h, m = map(int, input().split(" "))

min = (h * 60) + m - 45

hour = min // 60
min = min % 60

print(f'{hour} {min}')