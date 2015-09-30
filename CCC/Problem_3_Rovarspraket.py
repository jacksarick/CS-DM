# Teach the computer the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]
vowelnum = [0, 4, 8, 14, 20]

# Get the word we need, and set up a blank
word = list(raw_input().lower())
newword = ""

# Loop through the word
for letter in word:
	# vowels are easy
	if letter in vowels:
		# just pass the letter back
		newword += letter

	# we have more trouble if it's a consonant
	else:
		# add our original letter
		newword += letter

		# this is a wicked confusing thing that finds the closest vowel index
		closest = [abs(alphabet.index(letter) - val) for val in vowelnum]
		# converts vowel index to actual vowel
		newword += next_vowel(alphabet[vowelnum[closest.index(min(closest))]])

		# this just adds the next letter in the alphabet
		newword += alphabet[alphabet.index(letter) + 1]

print newword