import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.width(2)

screen = turtle.Screen()
screen.bgcolor("black")

def draw_portal(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    colors = ["green", "lime", "cyan", "blue"]

    for i in range(100):
        t.pencolor(colors[i % len(colors)])
        t.circle(i * 0.5)
        t.right(15)

def draw_particles():
    for _ in range(80):
        t.penup()
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        t.goto(x, y)
        t.pendown()
        t.pencolor("lime")
        t.dot(random.randint(3, 8))

def draw_energy_lines():
    t.pencolor("green")
    for _ in range(40):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        angle = random.randint(0, 360)
        t.setheading(angle)
        t.forward(random.randint(100, 300))

def draw_glow():
    t.penup()
    t.goto(0, -50)
    t.pendown()
    for i in range(20):
        t.pencolor("lightgreen")
        t.circle(80 + i * 2)

def main():
    draw_glow()
    draw_portal(0, 0)
    draw_energy_lines()
    draw_particles()
    t.hideturtle()
    screen.mainloop()

main()
