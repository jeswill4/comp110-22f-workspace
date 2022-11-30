"""Chris Ross paint along."""

import turtle as t

def tree(x: float, y: float) -> None:
    """"Paint a beautiful tree."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    trunk_length: float = 100.0
    UP: float = 90.0
    branch(UP, trunk_length)
    t.update()


def branch(angle: float, length: float) -> None:
    """Creates branch."""
    t.setheading(angle)
    t.forward(length)
    if length < 5.0:
        ...
    else:
        branch(angle + 25, length * 0.75)
        branch(angle - 25, length * 0.70)
        branch(angle + 30, length * 0.55)
        branch(angle - 30, length * 0.50)
        branch(angle + 40, length * 0.40)
        branch(angle - 40, length * 0.35)

        
    t.setheading(angle + 180)
    t.forward(length)

t.tracer(0, 0)
t.speed(0)
tree(0.0, 0.0)
t.done()


