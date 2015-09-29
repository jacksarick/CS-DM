#Problem J2: Happy or Sad
hcount, scount = 0, 0
words = list(raw_input())

for i in range(len(words) - 2):
	if (words[i] + words[i+1] + words[i+2]) == ":-)":
		hcount += 1

	elif (words[i] + words[i+1] + words[i+2]) == ":-(":
		scount += 1

if (hcount + scount) == 0:
	print "none"

elif (hcount == scount):
	print "unsure"

elif (hcount > scount):
	print "happy"

elif (hcount < scount):
	print "sad"