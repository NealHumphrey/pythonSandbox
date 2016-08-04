import turtle, math

def draw_polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.rt(angle)

def draw_arc(t,radius,degrees,direction):
	#always draws the arc clockwise
	circumference = 2 * math.pi * radius
	n = int(circumference / 3) + 1
	length = circumference / n

	angle = 360 / n

	count = int((degrees / 360) * n) + 1

	for i in range(count):
		t.fd(length)
		if direction == 'clockwise':
			t.rt(angle)
		else:
			t.lt(angle)



def draw_mushroom(t):
	base = 20

	#appearance
	color = "red"
	t.fillcolor(color)
	t.color(color)
	t.begin_fill()

	#draw base
	t.setheading(180)
	for i in range(3):
		t.left(90)
		t.forward(base)
	t.right(90)
	t.forward(base / 2)

	#draw top
	t.left(90)
	draw_arc(t,base,180,'counter')
	t.setheading(0)

	#close the mushroom
	t.forward(base / 2)
	t.end_fill()

def main():

	t = turtle.Turtle()

	t.hideturtle()
	t.pendown()
	t.speed('fastest')

	draw_mushroom(t)

	

#run the functions
main()
turtle.mainloop()
