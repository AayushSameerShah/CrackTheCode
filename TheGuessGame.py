## -- PERSONAL INSTRUCTIONS -- ##

# CLOSE : No numbers are matching but one or more than one of them are closer to the code
# MATCH : One or More numbers are matching in the code
# PERFECT : The Code is perfect !
# NOPE : None of the numbers are even nearby to the Code.

import random


def three(num):
	if len(str(num)) != 3:
		print('Fuck up, Enter the three digit code ONLY.')
		return False
	return True

def unique(num):
	snum = str(num)
	if (snum[0] == snum[1]) or (snum[0] == snum[2]) or (snum[1] == snum[2]):
		print("No Repeating characters you shit !")
		return False
	return True

def Generate():
	
	while True:
		theCode = random.randint(100,1000)
		# print("Trial : ",theCode)
		if unique(theCode) : break

	# print(theCode)
	return theCode

def checkDistance(num,code):
	if num == code:
		return ('p',num)
	if any([True if ch in str(code) else False for ch in str(num)]):
		return ('m',None)
	
	for nu in str(num):
		for co in str(code):
			if int(nu) - int(co) == 1:
				return ('c',None)

	return ('n',None)

	

def ask():
	while True:
		num = int(input('What do you say ? '))
		if not three(num): continue
		if unique(num) : return num


# Start the Code

print('--- Welcome to my World ---')
print("\nI challenge you that you can't brake my guesses code...\n if you can then... what? You will win !")

print('\nHere is what I have guessed : *** ')

theCode = Generate()


while True:

	num = ask()

	clue = checkDistance(num,theCode)
	
	if clue[0] in ['m','c','n']:
		if clue[0] == 'm':
			print('MATCH : One or More numbers are matching in the code')
			continue
		elif clue[0] == 'c':
			print('CLOSE : No numbers are matching but one or more than one of them are closer to the code')
			continue
		elif clue[0] == 'n':
			print('NOPE : None of the numbers are even nearby to the Code.')
			continue
	else:
		print('Man ! You have just cracked the code ! FUCK UP !\n The code is -> {code}\n\n Now open any gate of the world with this code... !'.format(code=clue[1]))
		break