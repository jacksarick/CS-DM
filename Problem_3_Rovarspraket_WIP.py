alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]
vowelnum = [0, 4, 8, 14, 20]

word = list(raw_input().lower())
newword = ""

def next_vowel(letter):
	global alphabet
	global vowels
	global vowelnum

	closest = [abs(alphabet.index(letter) - val) for val in vowelnum]
	return alphabet[minim.index(min(minim))]

for letter in word:
	if letter is in vowel:
		newword += letter

	else:
		newword += letter
		newword += next_vowel(letter)
		newword += alphabet[alphabet.index(letter) + 1]