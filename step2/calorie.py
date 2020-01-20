#calorie

# 3 가지의 버거 

# 1 . Cheeseburger (461 Calories) 
# 2 . Fish Burger (431 Calories) 
# 3 . Veggie Burger (420 Calories) 
# 4 . no burger 

# 3 가지 음료

# 1 . Soft Drink ( 130 Calories)
# 2 . Orange Juice (160 Calories)
# 3 . Milk (118 Calories)
# 4 . no drink

# 3 가지 side order(추가 주문)

# 1 . Fries (100 Calories)
# 2 . Baked Potato (57 Calories) 
# 3 . Chef Salad (70 Calories) 
# 4 . no side order 

# 3 가지 디저트 

# 1 . Apple Pie (167 Calories)
# 2 . Sundae (266 Calories)
# 3 . Fruit Cup (75 Calories)
# 4 . no dessert

a, b, c, d = map(int, input().split(" "))
menu1 = [461, 431, 420, 0]
menu2 = [130, 160, 118, 0]
menu3 = [100, 57, 70, 0]
menu4 = [167, 266, 75, 0]

print('Your total Calorie count is %d.' % (menu1[a - 1] + menu2[b - 1] + menu3[c - 1] + menu4[d - 1]))
