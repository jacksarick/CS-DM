# find the sum of a number
def sum_number(number):
	numbers = list(str(number))
	numbers = [int(character) for character in numbers]
	sum_of_numbers = sum(numbers)
	return sum_of_numbers

for number in range(1,100):
	if (sum_number(number) % 3 == 0) and (str(number)[-1] == "0" or str(number)[-1] == "5"):
		print "FizzBuzz"

	if (sum_number(number) % 3 == 0):
		print "Fizz"

	if (str(number)[-1] == "0" or str(number)[-1] == "5"):
		print "Buzz"
		
	else:
		print number