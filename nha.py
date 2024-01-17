import turtle
#Bước 2: Lấy ngòi viết
t=turtle.Turtle()
#nhấc ngòi viết
t.penup()
#Di chuyển đến bước cần vẽ
t.goto(-200,-200)
t.pendown()
#Tiến tới 100 đơn vị
t. forward(100)
#quay phải 90 độ
t.right(90)
#Tiến tới 100 đơn vị
t.forward(100)
# quay phải 90 độ
t.right(90)
# Tiến tới 100 đơn vị
t.forward(100)
#quay phải 90 độ
t.right(90)
#Tiến tới 100 đơn vị
t.forward(100)

#Xoay con trỏ lên 45 độ
t.right(45)
t.forward(80)
#Xoay con trỏ x độ
t.right(100)
t.forward(80)
#Ve hinh tron
t.penup()
t.goto(200,200)
t.pendown()
#Ve hinh tron co ban kinh la 50
t.circle(50)


turtle.done()
