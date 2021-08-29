import math
import random
import turtle

# Define several useful constants to be used by the Turtle graphics.
WIDTH = 960               # Usually 720, 960, 1024, 1280, 1600, or 1920.
HEIGHT = WIDTH * 9 // 16  # Produces the eye-pleasing 16:9 HD aspect ratio.
MARGIN = WIDTH // 30      # Somewhat arbitrary value, but it looks nice.
FONT_SIZE = MARGIN // 2   # Somewhat arbitrary value, but it looks nice.
DRAW_FAST = False         # Set to True for fast, non-animated turtle movement.

COLORS = [ "red", "green", "blue", "yellow", "cyan", "magenta", "white", "black" ]


def main():
    """Main program to test solutions for each exercise."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    # Call each individual exercise; comment/un-comment these lines as you work.
    # exercise0()
    # exercise1()
    exercise2()


class Point:
    """Point class for representing (x,y) coordinates."""

    # TODO 0a: Read, discuss, and understand the following code.
    def __init__( self, x=0, y=0 ):
        """Create a new Point with the given x and y values.
        :param int x: The x-coordinate; default is zero.
        :param int y: The y-coordinate; default is zero.
        """
        # Assign the x and y values passed as parameters as attributes of self.
        self.x = x
        self.y = y

    # TODO 0c: Read, discuss, and understand the following code.
    def draw( self, art ):
        """Draw this Point object using the given turtle.
        :param turtle.Turtle art: The turtle to use to draw this Point object.
        :return: None
        """
        # Use the self object's x and y values to set the heading.
        art.setheading( art.towards( self.x, self.y ) )
        # Use the self object's x and y values to move the turtle.
        art.setposition( self.x, self.y )
        # Draw a dot at the point.
        art.dot( 4 )


def exercise0():
    """Demonstrate a Point class."""
    # Create the turtle screen and two turtles (leave this as the first line).
    screen, artist, writer = turtle_setup()
    writer.write( "Creating and drawing Point objects...",
                  align="center", font=( "Times", FONT_SIZE, "bold" ) )

    # TODO 0b: Read, discuss, and understand the following code.
    points = []  # An empty list to be filled with Point objects.
    y = HEIGHT // 4  # Start the y-coordinate one-quarter screen height above the x-axis.
    # Loop through evenly spaced x-coordinates.
    for x in range( -WIDTH // 2 + MARGIN, WIDTH // 2 + MARGIN, ( WIDTH - MARGIN * 2 ) // 8 ):
        p = Point( x, y )  # Use the values of x and y to create a Point object.
        points.append( p )  # Appends the point to the list of point objects.
        y *= -1  # Modify y so the points alternate above and below the x-axis.

    # TODO 0d: Read, discuss, and understand the following code.
    # Loop through the list of Point objects and tell each to draw itself.
    for p in points:
        print( p, flush=True )
        # Tell the Point object to draw itself using the artist turtle.
        p.draw( artist )

    # Wait for the user to click before closing the window (leave this as the last line).
    artist.home()
    screen.exitonclick()


# TODO 1a: In the space below this comment, write the class as described in the lab document.
class Spot:
    """Spot class for representing (x,y) coordinates."""

    def __init__( self, x=0, y=0, color=""):
        """Create a new Spot with the given x and y values.
        :param int x: The x-coordinate; default is zero.
        :param int y: The y-coordinate; default is zero.
        :param string color: The color of the spot
        """
        # Assign the x and y values passed as parameters as attributes of self.
        self.x = x
        self.y = y
        self.color = color

    def __str__( self ):
        """Return a string representation of this object.
        :return: The Point object in the format (x,y).
        :rtype: str
        """
        return "({},{})".format( self.x, self.y )

    # TODO 0c: Read, discuss, and understand the following code.
    def draw( self, art ):
        """Draw this Point object using the given turtle.
        :param turtle.Turtle art: The turtle to use to draw this Point object.
        :return: None
        """
        # Use the self object's x and y values to set the heading.
        art.setheading( art.towards( self.x, self.y ) )
        # Use the self object's x and y values to move the turtle.
        art.setposition( self.x, self.y )
        # Draw a dot at the point.
        art.dot( 20, self.color )
        art.setposition( self.x + 10, self.y - 10 )
        art.dot( 15, self.color )
        art.setposition( self.x - 10, self.y - 10 )
        art.dot( 15, self.color )
        art.setposition( self.x, self.y - 15 )
        art.dot( 20, self.color )


def exercise1():
    """Test a Spot class."""
    # Create the turtle screen and two turtles (leave this as the first line).
    screen, artist, writer = turtle_setup()
    writer.write( "Creating and drawing Spot objects...",
                  align="center", font=( "Times", FONT_SIZE, "bold" ) )

    # TODO 1b: In the space below, use the class as described in the lab document.
    spots = []
    x = (-WIDTH / 2) + MARGIN
    y = (-HEIGHT / 2) + MARGIN
    x_shift = (WIDTH - (2 * MARGIN)) / 7
    y_shift = (HEIGHT - (2 * MARGIN)) / 7

    for i in range(8):
        s = Spot( x, y, COLORS[i] )
        s.draw(artist)
        x += x_shift
        y += y_shift


    # Wait for the user to click before closing the window (leave this as the last line).
    artist.home()
    screen.exitonclick()


# TODO 2a: In the space below this comment, write the class as described in the lab document.
class Raindrop:
    """Raindrop class for representing (x,y) coordinates."""

    def __init__( self ):
        """Create a new Raindrop with the given x and y values.
        :int x: The x-coordinate; default is zero.
        :int y: The y-coordinate; default is zero.
        :int radius: The radius of the raindrop
        """

        # Assign the x and y values passed as parameters as attributes of self.
        self.x = random.randint( -WIDTH // 2 + MARGIN, WIDTH // 2 - MARGIN )
        self.y = random.randint( -HEIGHT // 2 + MARGIN, HEIGHT // 2 - MARGIN )
        self.radius = random.randint( 25, 25 )

    def __str__( self ):
        """Return a string representation of this object.
        :return: The Point object in the format (x,y).
        :rtype: str
        """
        return "({},{}):{:.2f}".format( self.x, self.y, self.radius)

    def draw( self, art ):
        """Draw this Point object using the given turtle.
        :param turtle.Turtle art: The turtle to use to draw this Point object.
        :return: None
        """
        # Use the self object's x and y values to set the heading.
        art.setheading( art.towards( self.x, self.y ) )
        # Use the self object's x and y values to move the turtle.
        art.setposition( self.x, self.y )
        # Draw a dot at the point.
        art.dot( self.radius*2 )

    def area( self ):
        return math.pow( self.radius, 2 ) * math.pi

    def overlaps( self, other ):
        if math.hypot(self.x - other.x, self.y - other.y) <= (self.radius + other.radius):
            return True
        else:
            return False

    def expand( self, other, art ):
        total = self.area() + other.area()
        self.radius = math.sqrt(total // math.pi)


def exercise2():
    """Test a Raindrop class."""
    # Create the turtle screen and two turtles (leave this as the first line).
    screen, artist, writer = turtle_setup()
    writer.write( "Creating and drawing Raindrop objects...",
                  align="center", font=( "Times", FONT_SIZE, "bold" ) )

    # Make the artist turtle a blue circle for this application.
    # artist.color( 'blue' )
    # artist.shape( "circle" )

    # TODO 2b: In the space below, use the class as described in the lab document.
    raindrops = []  # An empty list to be filled with Point objects.
    stop = False
    while not stop:
        total_area = 0
        r = Raindrop()  # Calls the Point object's __init__ method to create a point object.

        # Have the writer turtle display the Point object's x and y values.
        writer.clear()
        writer.write( "Moving to point ({}, {})...".format( r.x, r.y ),
                      align="center", font=( "Times", FONT_SIZE, "bold" ) )

        print("Drawing new drop {}".format( r, flush=True ))
        r.draw( artist )

        for drop in raindrops:
            if r.overlaps(drop):
                r.expand( drop, artist )
                r.draw( artist )
                print("Expanding drop {}".format( r, flush=True))
            total_area += r.area()

        raindrops.append( r )  # Appends the point to the list of point objects.

        if total_area > (HEIGHT * WIDTH):
            stop = True

    # Wait for the user to click before closing the window (leave this as the last line).
    artist.home()
    screen.exitonclick()


def turtle_setup():
    """Setup the turtle environment with a screen and two turtles, one for drawing and one for writing.
    Using separate turtles for drawing and writing makes it easy to clear one or the other by
    doing artist.clear() or writer.clear() to clear only the drawing or writing, respectively.
    :return: The screen, a drawing turtle, and a writing turtle.
    :rtype: (turtle.Screen, turtle.Turtle, turtle.Turtle)
    """
    #  ___   ___     _  _  ___ _____    __  __  ___  ___ ___ _____   __
    # |   \ / _ \   | \| |/ _ \_   _|  |  \/  |/ _ \|   \_ _| __\ \ / /
    # | |) | (_) |  | .` | (_) || |    | |\/| | (_) | |) | || _| \ V /
    # |___/ \___/   |_|\_|\___/ |_|    |_|  |_|\___/|___/___|_|   |_|
    #  _____ _  _ ___ ___    ___ _   _ _  _  ___ _____ ___ ___  _  _
    # |_   _| || |_ _/ __|  | __| | | | \| |/ __|_   _|_ _/ _ \| \| |
    #   | | | __ || |\__ \  | _|| |_| | .` | (__  | |  | | (_) | .` |
    #   |_| |_||_|___|___/  |_|  \___/|_|\_|\___| |_| |___\___/|_|\_|
    #
    # Create the turtle graphics screen and set a few basic properties.
    screen = turtle.Screen()
    screen.setup( WIDTH, HEIGHT, MARGIN, MARGIN )
    screen.bgcolor( "SkyBlue" )

    # Create two turtles, one for drawing and one for writing.
    artist = turtle.Turtle()
    writer = turtle.Turtle()

    # Change the artist turtle's shape so the artist and writer are distinguishable.
    artist.shape( "turtle" )
    # Lift the artist's pen and slow it down to see the movements from object to object.
    artist.penup()
    artist.speed( "slowest" )

    # Make the animation as fast as possible and hide the turtles.
    if DRAW_FAST:
        screen.delay( 0 )
        artist.hideturtle()
        artist.speed( "fastest" )
        writer.hideturtle()
        writer.speed( "fastest" )

    # Set a few properties of the writing turtle useful since it will only be writing.
    writer.setheading( 90 )   # Straight up, which makes it look sort of like a cursor.
    writer.penup()            # A turtle's pen does not have to be down to write text.
    writer.setposition( 0, HEIGHT // 2 - FONT_SIZE * 2 )  # Centered at top of the screen.

    return screen, artist, writer


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()