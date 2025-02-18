from turtle import*

def dessiner_spirale():
    begin_fill()
    speed(12)
    bgcolor('black')
    color('red')
    b = 200
    while b > 0:
        right(b)
        forward(b * 3)
        b = b - 1
    end_fill()

dessiner_spirale()

nouvelle_position_x = 500
nouvelle_position_y = 300
penup
goto(nouvelle_position_x, nouvelle_position_y)
pendown

dessiner_spirale()

done()
