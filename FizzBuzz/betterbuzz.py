# find the sum of a number
def sum_number(number):
	numbers = list(str(number))
	numbers = [int(character) for character in numbers]
	sum_of_numbers = sum(numbers)
	return sum_of_numbers

for i in range(1,100):
	pass