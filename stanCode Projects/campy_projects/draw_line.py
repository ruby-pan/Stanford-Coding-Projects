"""
File: draw_line.py
Name: Ruby
-------------------------
This file uses campy module to
draw lines on a GWindow object
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 30
window = GWindow()
if_ball = False
ball = GOval(SIZE, SIZE)

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(check)

def check(m):
    """
    To see if ball is there. If not, add ball.
    If so, remove ball and add a line.
    """
    global if_ball
    if if_ball is False:
        ball.filled = False
        window.add(ball, x=m.x - SIZE / 2, y=m.y - SIZE / 2)
        if_ball = True

    else:
        window.remove(ball)
        line = GLine(ball.x + SIZE/2, ball.y+SIZE/2, m.x, m.y)
        window.add(line)
        if_ball = False


if __name__ == "__main__":
    main()
