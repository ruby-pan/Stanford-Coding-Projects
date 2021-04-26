"""
File: bouncing_ball.py
Name: Ruby
-------------------------
This file uses campy module to
simulate ball bouncing on a GWindow object
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
num = 0

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, START_X, START_Y)
    onmouseclicked(drop)

def drop(m):
    """
    To initiate the drop of ball.
    """
    global num
    shift = 0
    if num >= 3:    # If num equals 3 times, then the function 'drop' stops
        pass
    else:
        while True:
            ball.move(VX, shift)
            if ball.y >= window.height-2*SIZE:  # If ball touches bottom, change the direction of speed.
                shift = -shift
                shift = REDUCE*shift
            elif ball.x >= window.width :      # If ball exceeds window width, start at beginning.
                ball.x = START_X
                ball.y = START_Y
                num += 1
                break
            else:
                pass
            shift += GRAVITY
            pause(DELAY)


if __name__ == "__main__":
    main()
