import random
import turtle
from _engine import t, USE_SVG

# Enable RGB color tuples (0-255) so students can easily use the Google Color Picker
turtle.colormode(255)

# --- BASELINE EXAMPLES ---
def draw_bubble(x, y, radius):
    """
    Draws a single circular bubble using turtle commands.
    
    Args:
        x (int): The x-coordinate for the center of the bubble.
        y (int): The y-coordinate for the center of the bubble.
        radius (int): The size of the bubble.
        
    Returns:
        None
    """
    t.color("white")      # or "lightblue", "gray", etc.

    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)

def draw_seaweed(x, y, segments, color_name):
    """
    Draws a wavy stalk of seaweed.
    
    Args:
        x (int): The starting x-coordinate for the seaweed.
        y (int): The starting y-coordinate (usually the tank floor).
        segments (int): How tall the seaweed should grow.
        color_name (str): The color of the seaweed.
        
    Returns:
        None
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color_name)
    t.pensize(4)
    t.setheading(90) # Point straight up
    
    # A simple loop to make the seaweed look wavy
    for _ in range(segments):
        t.forward(15)
        t.right(15)
        t.forward(15)
        t.left(15)


# --- STUDENT FUNCTIONS ---
def draw_tank(build_left, build_bottom, build_right, build_top):
    """
    Draws the 4 walls of the rectangular fish tank using the turtle.
    
    Args:
        build_left (bool): If True, draws the left wall.
        build_bottom (bool): If True, draws the floor of the tank.
        build_right (bool): If True, draws the right wall.
        build_top (bool): If True, draws the lid of the tank.
        
    Returns:
        None
    """
    t.color("black")
    t.pensize(5)
    t.fillcolor("lightblue")
    t.begin_fill()


    # BUG 1.1: The tank is invisible and empty!
    # TODO: Use t.color() and t.pensize() to set the color and thickness of the glass.
    # TODO: Use t.fillcolor() and t.begin_fill() to set the water color.

    t.penup()
    t.goto(-380, 280)
    t.setheading(270) 
    
    for i in range(4):
        # BUG 1.2: The water spills out! 
        # TODO: Write an if/elif chain to control the pen.
        # Check which wall is being drawn (i) AND if its matching boolean argument is True.
        # Walls: left=0, bottom=1, right=2, top=3. 
        # Call t.pendown() if the wall should be built, otherwise call t.penup().
        
        if (i) in range(4) and True:
            t.pendown()
        else:
            t.penup()

        # Draws the rectangular shape slightly smaller than the canvas
        if i % 2 == 0:
            t.forward(560) # Vertical walls
        else:
            t.forward(760) # Horizontal walls
        t.left(90)
        
    t.end_fill()


# TODO: Architect your custom helper functions here (e.g., draw_fish, draw_crab).
# You must include a full docstring (with Args and Returns) for each function!

def draw_fish(x, y, size, is_facing_left):
    """
    Draws a fish.

    Args:
        x (int): X-coordinate of the fish.
        y (int): Y-coordinate of the fish.
        size (int): Size of the fish.
        is_facing_left (bool): Direction the fish faces.

    Returns:
        None
    """
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.color("orange")
    t.begin_fill()
    t.circle(size)
    t.end_fill()

    # Tail
    if is_facing_left:
        t.penup()
        t.goto(x + size, y)
        t.setheading(0)
    else:
        t.penup()
        t.goto(x - size, y)
        t.setheading(180)

    t.pendown()
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def draw_creature(creature_type, x, y, size, is_facing_left):
    if creature_type == "fish" and is_facing_left:
        draw_fish(x, y, size, True)

    elif creature_type == "fish" and not is_facing_left:
        draw_fish(x, y, size, False)

    else:
        print("Unknown creature type")
    # BUG 4: The tank is empty! (Capstone Task)
    # TODO: Write if/elif/else logic using 'and' to call your custom drawing 
    # functions based on the creature_type and is_facing_left parameters.
    # Example: if creature_type == "fish" and is_facing_left:
    


def draw_environment():
    """
    Draws the background elements of the tank, including bubbles and seaweed.
    
    Args:
        None
        
    Returns:
        None
    """
    for x in range(-300, 301, 50):
        if x % 2 == 0:
            draw_seaweed(x, -280, 8, "green")
        else:
            draw_seaweed(x, -280, 12, "darkgreen")
    y = -200
    while y < 280: 
        # Uses a random integer to shift the x position back and forth naturally
        random_x = random.randint(-230, -170)
        draw_bubble(random_x, y, 10)
        y += 60
        
    # BUG 3: No seaweed! 
    # TODO: Write a 'for' loop using range() across the x-axis (e.g., from -300 to 300). 
    # Inside the loop, use an if/else block with the modulus operator (%) 
    # to call draw_seaweed() with alternating heights or colors.
    


def main():
    draw_tank(True, True, True, True)

    draw_environment()

    fish_data = [
        (-100, 0, 20, True),
        (100, 50, 25, False),
        (0, -100, 15, True)
    ]

    for x, y, size, facing_left in fish_data:
        draw_creature("fish", x, y, size, facing_left)
    # TODO: Call draw_creature() multiple times inside a loop to populate the tank.
    # Make sure to test passing both True and False for the is_facing_left parameter!

if __name__ == "__main__":
    main()
    
    if USE_SVG:
        t.save_as('my_fishtank.svg')
        print("Successfully saved my_fishtank.svg")
    else:
        # Prevents the turtle window from closing immediately after finishing
        turtle.done()