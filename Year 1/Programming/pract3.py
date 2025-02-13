from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry


def hello_graphix():
    win = Window()
    message = Text(Point(200, 200), "hello graphix!")
    message.draw(win)


def draw_stick_figure():
    win = Window()
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)


def draw_line():
    win = Window()
    message = Text(Point(200, 50), "click on first point")
    message.draw(win)
    p1 = win.get_mouse()
    message.text = "click on second point"
    p2 = win.get_mouse()
    line = Line(p1, p2)
    line.draw(win)
    message.text = "click anywhere to quit"
    win.get_mouse()
    win.close()


# Solutions below:
def draw_stick_figure():
    win = Window()

    head = Circle(Point(200, 120), 40)
    head.draw(win)
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)
    leg1 = Line(Point(200, 240), Point(160, 280))
    leg2 = Line(Point(200, 240), Point(240, 280))
    
    legs = [leg1, leg2]
    
    for leg in legs:
        leg.draw(win)

def draw_archery_target():
    win = Window("Anchery Target")
    
    base_radius = 60
    
    middle_x, middle_y = abs(win.width // 2), abs(win.height // 2)

    yellow = Circle(Point(middle_x, middle_y), base_radius)
    yellow.fill_colour = "yellow"

    red = Circle(Point(middle_x, middle_y), base_radius * 2)
    red.fill_colour = "red"

    blue = Circle(Point(middle_x, middle_y), base_radius * 3)
    blue.fill_colour = "blue"

    blue.draw(win)
    red.draw(win)
    yellow.draw(win)

def draw_rectangle():
    win = Window("Draw Rectangle")
    
    middle_x, middle_y = abs(win.width // 2), abs(win.height // 2)

    height = int(input("What height would you like the rectangle to be? >"))
    width = int(input("What width would you like the rectangle to be? >"))

    rec_p1_x = middle_x + abs(height // 2)
    rec_p1_y = middle_y + abs(width // 2)
    rec_p2_x = middle_x - abs(height // 2)
    rec_p2_y = middle_y - abs(width // 2)

    rec = Rectangle(Point(rec_p1_x, rec_p1_y), Point(rec_p2_x, rec_p2_y))
    rec.draw(win)

def blue_circle():
    win = Window("Draw Blue Circle", 600, 600)

    middle_x = abs(win.width // 2)

    msg = Text(Point(middle_x, 10), "Click anywhere to draw a circle")
    msg.draw(win)
    
    circle_location = win.get_mouse()

    the_blue_circle = Circle(circle_location, 100)
    the_blue_circle.fill_colour = "blue"
    the_blue_circle.draw(win)

    win.get_mouse()

def draw_ten_lines():
    win = Window()

    for _ in range(1, 11):
        message = Text(Point(200, 50), "click on first point")
        message.draw(win)
        p1 = win.get_mouse()
        message.text = "click on second point"
        p2 = win.get_mouse()
        line = Line(p1, p2)
        line.draw(win)

        message.undraw()

    message.text = "click anywhere to quit"
    win.get_mouse()
    win.close()

def ten_strings():
    win = Window()

    middle_x = abs(win.width // 2)

    text_box_width = 20

    text_box_message = Text(Point(middle_x, 20), "Enter the string text then click anywhere to !")
    text_box_message.draw(win)

    for _ in range(11):
        text_box = Entry(Point(middle_x, 40), text_box_width)
        text_box.draw(win)

        

    win.get_key()

ten_strings()