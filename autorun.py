import os
from pathlib import Path
import time

PASSWORD = ''

length = 0
file = open('ctest.txt')

command_1 = 'curl -OL https://golang.org/dl/go1.17.4.linux-amd64.tar.gz'
command_2 = f'echo {PASSWORD} | sudo -S tar -C /usr/local -xvf go1.17.4.linux-amd64.tar.gz'
command_3 = 'export PATH=$PATH:/usr/local/go/bin'
command_4 = 'gaiad config node node_address'
command_5 = 'export PATH=$PATH:$(go env GOPATH)/bin && echo {password} | gaiad keys add {number} --recover'
command_6 = 'gaiad tx bank send {number} atom_address 100000000uatom --fees 5000uatom -y'


for line in file:
	goose = len(line.split())
	length = length + 1
	if goose == 12:
		if line.startswith('relayed'):
			continue
		elif line.startswith('Relayed'):
			continue
		else:
			passwords = line
			os.system(command_1)
			os.system(command_2)
			os.system(command_3)
			os.system(command_4)
			for i, password in enumerate(passwords, 1):
				os.system(command_5.format(password=password, number=i))
				os.system(command_6.format(number=i))
	elif goose == 24:
		passwords = line
		os.system(command_1)
		os.system(command_2)
		os.system(command_3)
		for i, password in enumerate(passwords, 1):
			os.system(command_5.format(password=password, number=i))
			os.system(command_6.format(number=i))




#Execute command to open session
# os.system('cmd /k "curl -OL https://golang.org/dl/go1.17.4.linux-amd64.tar.gz & sudo tar -C /usr/local -xvf go1.17.4.linux-amd64.tar.gz export PATH=$PATH:/usr/local/go/bin & export PATH=$PATH:$(go env GOPATH)/bin"')
# file = open('1.txt')
# for line in file:
#iterate through each line in file and import them into successive commands
	# os.system('cmd /k "gaiad keys add #iterating_number --recover & #each_line_in_file"')
