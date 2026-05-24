from turtle import *

Screen().setup(1.0, 1.0)
delay(50)

# переносимось на координати човна
up()
goto(-60, -250)
down()

# малюлємо човен
fillcolor('brown')
begin_fill()
goto(-90, -300)
goto(-200, -300)
goto(-230, -250)
goto(-60, -250)
end_fill()

# переносимось на координати щогли
up()
goto(-150, -250)
down ()

# малюємо щоглу
goto(-150, -90)

# малюємо вітрило
fillcolor('red')
begin_fill()
goto(-110, -130)
goto(-150, -170)
end_fill()

# малюємо хвилі
color('blue')
up()
goto(-270, -270)
down()
goto(-250, -270)

up()
goto(-40, -280)
down()
goto(20, -280)
goto(20, -270)

up()
goto(30, -280)
down()
goto(30, -290)
goto(10, -290)

# малюємо кита
color('blue', 'blue')
begin_fill()
up()
goto(200, -300)
down()
left(90)
circle(37, 180)
goto(240, -300)
goto(240, -270)
goto(200, -300)
end_fill()

# переходимо на координати ока
up()
goto(160, -280)
down()

# малюємо око
dot(10)

# переходимо на координати сонця 
color('orange', 'orange')
up()
goto(-190, 170)
down()

# малюємо сонце 
begin_fill()
left(90)
circle(70)
end_fill()

done()