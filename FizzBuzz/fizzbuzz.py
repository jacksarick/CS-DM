for number in range(100):
	if number % 3 == 0 and number % 5 == 0:
		print "FizzBuzz"

	if number % 5 == 0:
		print "Buzz"

	if number % 3 == 0:
		print "Fizz"

	else:
		print number