"""Demonstrations of dictionary capabilities."""

# Declaring the type of a dictionary
schools: dict[str, int] 

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["DUKE"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key 
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# by its key.
schools.pop("DUKE")

# Test for the existence of a key
is_duke_present: bool = "DUKE" in schools
print(f"Duke is present: {is_duke_present}")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["DUKE"] = 0
if "DUKE" in schools:
    print("Found the key 'DUKE' in schools.")
else:
    print("No key 'DUKE' in schools.")

schools["NCSU"] = 20000
print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {} # Same as dic()
print(schools)
# alternatively, initialize key-value pairs
schools = {"UNC": 19400, "DUKIE": 6717, "NCSU": 26150}
print(schools)

# What happens when a key does not exist?
# print(schools["UNCC"])
# gives KeyError: 'UNCC'

# This works
points: dict[str, int] = {"Kris": 0, "Kaki": 10}
points["Kaki"] += 100
print(points)

