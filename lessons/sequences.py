"""Notes and examples of tuple and range sequence types."""

# Declaring a type alias that "invents" the Point2d type
Point2D = tuple[float, float]

start_position: Point2D = (5.0, 10.0)
# can't change individual items in it, not like a list that can be popped or appended
start_posiiton = (start_position[0] + 5.0, start_position[1] + 10.0)
print(start_position)

