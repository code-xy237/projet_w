from turtle import*
begin_fill()
speed(10)
color('cyan')
bgcolor('black')
b = 200
while b > 0:
    right(b)
    forward(b * 3)
    b = b - 1
end_fill()
