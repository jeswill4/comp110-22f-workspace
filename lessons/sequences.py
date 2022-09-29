"""Notes and examples of tuple and range sequence types."""

# Declaring a type alias that "invents" the Point2d type
Point2D = tuple[float, float]
# Camel casing, no underscoring and capitalizing starting letters of words
# Traced outline of word it looks like a camel back
# Gives us hint that type was made by us not python type

start_position: Point2D = (5.0, 10.0)
print(start_position)
# can't change individual items in it, not like a list that can be popped or appended
start_position = (start_position[0] + 5.0, start_position[1] + 10.0)
print(start_position)
end_position: Point2D = (99.0, 99.0)

# tupels, because they are a sequence, are 0-indexed)
print(start_position[0])

for item in end_position:
    print(item)

print(len(end_position))

