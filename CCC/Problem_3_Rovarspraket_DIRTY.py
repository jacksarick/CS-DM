alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

vowel = ["a", "e", "i", "o", "u"]
vowelnum = [0, 4, 8, 14, 20]

output = []

word = list(raw_input().lower())

def isVowel(letter):
	if letter in vowel:
		return True

def nextVowel(letter):
	tempnums = []
	for i in range(len(vowelnum)):
		tempnums.append(abs(vowelnum[i] - alph.index(letter)))
	return vowel[tempnums.index(min(tempnums))]


def nxtconst(letter):
	if letter == "z":
		return "z"

	elif alph[alph.index(letter) + 1] in vowel:
		return alph[alph.index(letter) + 2]

	else:
		return alph[alph.index(letter) + 1]

def replace(letter):
	return letter + nextVowel(letter) + nxtconst(letter)

for i in range(len(word)):
	if isVowel(word[i]):
		output.append(word[i])
	else:
		output.append(replace(word[i]))

print "".join(output)