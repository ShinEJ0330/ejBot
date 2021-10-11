#Lab2. 내가 원하는 원 그리기
import turtle as t

t.shape("turtle")
t.color("blue")
t.speed(0)
radius = int(input("원의 반지름을 입력하세요"))
t.begin_fill()
t.circle(radius)
t.end_fill()
