#Problem J2: Happy or Sad
# I've included 3 different methods for counting and 2 methods for producing an answer (from simplest to most advanced)
words = list(raw_input())

# Word Splice 1 (repetition)
hcount, scount = 0, 0
for i in range(len(words) - 2):
	if (words[i] + words[i+1] + words[i+2]) == ":-)":
		hcount += 1

	elif (words[i] + words[i+1] + words[i+2]) == ":-(":
		scount += 1

# Word Splice 2 (same as one, uses better splices)
hcount, scount = 0, 0
for i in range(len(words) - 2):
	if (words[i:(i+2)]) == ":-)":
		hcount += 1

	elif (words[i:(i+2)]) == ":-(":
		scount += 1

# Word Splice 3 (built in function)
hcount, scount = words.count(":-)"), words.count(":-(")

# Logic for all three (USE THIS)
if (hcount + scount) == 0:
	print "none"

elif (hcount == scount):
	print "unsure"

elif (hcount > scount):
	print "happy"

elif (hcount < scount):
	print "sad"

# PLEASE NEVER DO THIS
# It works, is very short, and runs in the same amount of time, but totally horrible
answers = [0, "none", "unsure", "happy", "sad"]
print answers[(((hcount + scount) == 0) + (2 * (hcount == scount)) + (3 * (hcount > scount)) + (4 * (hcount < scount)))]