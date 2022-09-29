"""Notes and examples of tuple and range sequence types."""

# Declaring a type alias that "invents" the Point2d type
Point2D = tuple[float, float]
# Camel casing, no underscoring and capitalizing starting letters of words
# Traced outline of word it looks like a camel back
# Gives us hint that type was made by us not python type
start_position: Point2D = (5.0, 10.0)
print(start_position)
# can't change individual items in it, not like a list that can be popped or appended
# tupels, because they are a sequence, are 0-indexed)
start_position = (start_position[0] + 5.0, start_position[1] + 10.0)
print(start_position)
end_position: Point2D = (99.0, 99.0)
for item in end_position:
    print(item)

print(len(end_position))


# examples of ranges
a_range: range = range(0, 10, 1)
# access its items
print("first item in range of 0-10:", a_range[0])
print("fourth item in range of 0-10:", a_range[4])
print("length of range 0-10:", len(a_range))
for i in a_range:
    print("index:", i)

# an example of using the default parameter step
# where the default step is 1
another_range: range = range(0, 10) 
# if you only pass one argument to range, it specifies
# the stop marker adn start is 0 by default
zero_start: range = range(10)
for x in zero_start:
    print("simple:", x)


