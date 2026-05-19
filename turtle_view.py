import turtle

SCALE = 4

def draw_point(t,x,y,color,size=6):
    t.penup()
    t.goto(x * SCALE, y * SCALE)
    t.pendown()
    t.dot(size,color)

def draw_border(t, size):
    limit = size * SCALE

    t.penup()
    t.goto(-limit, -limit)
    t.pendown()
    for _ in range(4):
        t.forward(limit * 2)
        t.left(90)

def draw_path(t,history):
    if not history:
        return
    
    t.penup()
    start = history[0]
    t.goto(start[0] * SCALE, start[1] * SCALE)
    t.pendown()

    for x, y in history:
        t.goto(x * SCALE, y * SCALE)


def draw_world(world, history):
    screen = turtle.Screen()
    screen.title("WYPRAWA W KOSMOS (symulacja)")
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    t.color("cyan")

    draw_border(t, world.size)

    draw_point(t, 0, 0, "green", 10)

    for x, y in getattr(world, "danger_zones", []):
        draw_point(t, x, y, "red", 6)

    for x, y in getattr(world, "energy_zones", []):
        draw_point(t, x, y, "yellow", 6)

    for x, y in getattr(world, "repair_stations", []):
        draw_point(t, x, y, "blue", 6)

    if hasattr(world, "core_position"):
        cx, cy = world.core_position
        draw_point(t, cx, cy, "purple", 12)

    draw_path(t, history)

    if history:
        last = history[-1]
        draw_point(t, last[0], last[1], "white", 10)

    t.hideturtle()
    turtle.done()