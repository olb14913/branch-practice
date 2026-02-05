for i in range(15, 22+1):
	if i % 3 == 0 or i % 5 == 0 :
		print('fizzbuzz' * (i%3==0) + 'buzz' * (i%5==0))
	else:
        	print(i)
