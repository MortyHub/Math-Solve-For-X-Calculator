import random

x = 0.0
value = 0.0
add = 0.0
multi = 0.0
choice = None

def start():
	x = 0.0
	value = 0.0
	add = 0.0
	multi = 0.0
	print('Choose Your Option')
	print('Equation Generator With answer(1), Solve For X(2), Solve For Value(3). (keep in mind this is only 2 step equations and fractions dont work.. ) Please Input The Number You Want To Select')
	choice = input()
	if choice == '1':
		gen()
	else:
		if choice == '2':
			sx()
		else:
			if choice == '3':
				sv()
			else:
				print('Invalid Choice')
				start()

def gen():
	value = random.randrange(-5000,5000)
	add = random.randrange(-100, 1000)
	multi = random.randrange(-100, 3050)

	print(str(multi) + 'x + ' + str(add) + ' = ' + str(value))
	z = value - add
	y = z / multi

	print('answer: ' + str(y))
	start()

def sx():
	print('Please Insert Your Value: ')
	value = int(input())
	print('Please Insert How Much x Is Being Multipled By: ')
	multi = int(input())
	print('Please Insert How Much Its Adding By (If Its Subtracting Then Put That Number As A Negative): ')
	add = int(input())
	if(add < 0):
		multi1 = multi - multi
		multi = multi1 + multi
		a = value - add
		b = a / multi
		print('Your Answer Is: ' + str(b))
	else:
	 	a = value - add
	 	b = a / multi
	 	print('Your Answer Is: ' + str(b))
	start()

def sv():
	print('Please Insert The Value Of x: ')
	x = int(input())
	print('Please Insert The Value Of What x Is Being Multiplied By')
	multi = int(input())
	print('Please Insert The Number Its Being Added By, If Its Subtracting Then Please Just Make That Number A Negative')
	add = int(input())
	c = multi * x
	d = c + add
	print('Your Answer Is: ' + str(d))
	start()
start()



