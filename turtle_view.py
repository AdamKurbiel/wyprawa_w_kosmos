import turtle

SCALE = 4

screen = None
t = None
initialized = False


def setup_screen():
    global screen
    screen = turtle.Screen()
    screen.title("WYPRAWA W KOSMOS - symulacja 2D")
    screen.bgcolor("black")
    screen.tracer(0)
    return screen


def create_turtle():
    global t
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    t.hideturtle()
    return t


def draw_point(x, y, color, size=6):
    t.penup()
    t.goto(x * SCALE, y * SCALE)
    t.pendown()
    t.dot(size, color)


def draw_border(size):
    limit = size * SCALE

    t.pencolor("cyan")
    t.penup()
    t.goto(-limit, -limit)
    t.pendown()

    for _ in range(4):
        t.forward(limit * 2)
        t.left(90)

def draw_legend(t):
    t.penup()
    t.goto(-300,300)
    t.pendown()
    t.pencolor("white")

    legend = [
        ("START","green"),
        ("ENERGIA","yellow"),
        ("ANOMALIA","red"),
        ("STACJA NAPRAWCZA", "blue"),
        ("RDZEŃ", "purple"),
        ("STATEK", "white")
    ]

    t.penup()
    y = 300
    for text, color in legend:
        t.goto(-320,y)
        t.dot(10,color)
        t.write(text, font=("Arial", 10, "normal"))
        y -= 25
    
    t.penup()
    



def init_world(world,vehicle):
    reset_view()
    global initialized

    if initialized:
        return

    setup_screen()
    create_turtle()

    draw_border(world.size)

    draw_point(vehicle.x, vehicle.y, "green", 10)

    for x, y in getattr(world, "danger_zones", []):
        draw_point(x, y, "red", 6)

    for x, y in getattr(world, "energy_zones", []):
        draw_point(x, y, "yellow", 6)

    for x, y in getattr(world, "repair_stations", []):
        draw_point(x, y, "blue", 6)

    if hasattr(world, "core_position"):
        cx, cy = world.core_position
        draw_point(cx, cy, "purple", 12)

    t.penup()
    t.goto(vehicle.x * SCALE,vehicle.y * SCALE)
    

    draw_legend(t)
    screen.update()
    initialized = True


def draw_step(history):
    if not history:
        return

    x, y = history[-1]

    t.pencolor("white")

    draw_point(x, y, "white", 6)

    if len(history) > 1:
        px, py = history[-2]

        t.penup()
        t.goto(px * SCALE, py * SCALE)
        t.pendown()
        t.goto(x * SCALE, y * SCALE)
    
    
    screen.update()


def reset_view():
    global initialized, screen, t

    initialized = False

    if screen:
        screen.clearscreen()