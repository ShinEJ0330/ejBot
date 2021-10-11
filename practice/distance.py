# 두 점 사이 거리 구하기
import math

x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))

distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

print(distance)
