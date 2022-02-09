# Braydon McElroy
# Euclid's algorithm: Largest tile problem 
# 05-11-21
# Algorithm: Solution 
# Version: 1.1.0

# Function to give us the smallest value
def min_value(width, height): 
	if(width > height): 
		return height 
	else: 
		return width
# Create our Rectangular area 
width = 150
height = 345
print(f"Square height: {height} width: {width}")
# Running our algorithm 
runtimeFlag = True
while(runtimeFlag): 
	# Get our min value from our two number values 
	min = min_value(width, height)

	# Begin placing our squares, if they fit
	if (min == width): 
		while(min < height): 
			height = height - min
	else: 
		while(min < width): 
			width = width - min
	# Checking values
	print(f"Square height: {height} width: {width}")
	# Check if our algorithm needs to finish
	if(width == height):
		runtimeFlag = False
# Send output
print(f"\nThe largest tile we can fit is {height} x {width}.")