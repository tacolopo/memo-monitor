count = 0  
length = 0
file = open('ctest.txt')

for line in file:
	goose = len(line.split())
	length = length + 1
	key = line.split()
	for word in key:
		if len(word.strip()) == 64:
	 		print('priv key')
	 		print(word)
	 		count = count + 1
	if goose == 12:
		if line.startswith('relayed'):
			continue
		elif line.startswith('Relayed'):
			continue
		else:
			print('twelve')
			print(line)
			count = count + 1
	elif goose == 24:
		print('24')
		print(line)
		count = count + 1
print(count, '|', length)


#priv keys are 64 character strings unhexed but so are tx hashes. 
