# Braydon McElroy
# Euclid's algorithm: Largest tile problem 
# 05-11-21
# Algorithm: Skeleton 
# Version: 1.0.0

# Function that takes two params to determine which is the min value and then 
# returns it 
def min_value(width, height): 
	# Implement the necessary logic to determine which of the two params are the 
	# min value and then return it. 
	# TODO #


# Create our Rectangular area. Feel free to change the values for testing 
width = 150
height = 345
# Print given dimensions
print(f"Square height: {height} width: {width}")

# Running our algorithm 
runtimeFlag = True
while(runtimeFlag): 
	# Utilize the provided min_value function to fetch the minimum value between 
	# the two dimension values
	# TODO #

	# Loop thru and determine which value you need to reduce using the value 
	# that you got above from min_value. Be sure to check which value you need 
	# to reduce for the algorithm to run correctly. 
	# TODO # 

	# Feel free to add print statements to trace your algorithm for debugging
	# TODO #
	
	# Add a condition to trip whenever the conditions are met. Change the 
	# runtimeFlag to false when the condtion is met and the loop needs to end. 
	# TODO


# Prints the output whenever the algorithm has completed. 
print(f"\nThe largest tile we can fit is {height} x {width}.")