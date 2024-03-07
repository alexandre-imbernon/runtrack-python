for chiffres in range(1, 101):
	if chiffres % 3 == 0 and chiffres % 5 == 0:
		print ("FizzBuzz")
	elif chiffres % 3 == 0:
		print ("Fizz")
	elif chiffres % 5 == 0:
		print ("Buzz")
	else:
    		print(chiffres)

