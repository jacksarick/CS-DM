#Problem J1: Special Day
date = int("".join([raw_input(), raw_input()]))
if (date == 218):
	print "Special"
elif (date > 218) or (int(firstinput[0]) >= 3):
	print "After"
else:
	print "Before"