import turtle, math


def square(t,length):

	angle = 90 #degrees in square

	for i in range(4):
		t.fd(length)
		t.lt(angle)

def polygon(t,length,sides):

	angle = 360 / sides

	for i in range(sides):
		t.fd(length)
		t.lt(angle)

def circle(t,radius):
	sides = 100
	angle = 360 / sides
	circumference = 2 * math.pi * radius
	length = circumference / sides

	for i in range(sides):
		t.fd(length)
		t.lt(angle)


bob = turtle.Turtle()


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


#execute the function
draw(bob,30,5)
turtle.mainloop()