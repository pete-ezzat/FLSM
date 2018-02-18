import os

# Get the Bit Combinations
def binary_compinations(n):
	host_bits = []
	
	for bit in range(1<<n):
		combination = bin(bit)[2:]
		combination = '0' * (n- len(combination))+combination
		host_bits.append(combination)
		
	return host_bits

#.#.#.

# Get Full Subnetmask
def full_subnetmask(subnet_mask):
	
	subnet_mask = int(subnet_mask)
	
	ones = subnet_mask * '1'
	zeros = '0' * (32 - subnet_mask)
	
	subnetmask_binary = ones + zeros
	
	octet1 = int(subnetmask_binary[0:8], 2)
	octet2 = int(subnetmask_binary[8:16], 2)
	octet3 = int(subnetmask_binary[16:24], 2)
	octet4 = int(subnetmask_binary[24:32], 2)
	
	subnetmask_decimal = str(octet1) + '.' + str(octet2) + '.' + str(octet3) + '.' + str(octet4)
	
	print('Subnet mask:', subnetmask_decimal, '\n')

#.#.#.

# Get the IP Class
def get_class(ip):
	
	octet1 = ip.split('.')
	octet1 = octet1[0]
	octet1 = int(octet1)
	
	if   octet1 < 128 : ip_class = 'A'
	elif octet1 < 192 : ip_class = 'B'
	elif octet1 < 224 : ip_class = 'C'
	elif octet1 < 240 : ip_class = 'D'
	elif octet1 < 256 : ip_class = 'E'
	
	return ip_class

#.#.#.

def calculate_subnets(ip):
	
	ip_class = get_class(ip)
	print("Class:", ip_class)
	
	subnet_mask = ip.split('/')
	ip = subnet_mask[0]
	
	subnet = int(subnet_mask[1])
	full_subnetmask(subnet)
	
	octets = subnet_mask[0].split('.')

	# Class A Calculations
	if ip_class == 'A':
		ip_start = octets[0] + '.'
		subnets_bits = subnet - 8
		host_bits = 24 - subnets_bits
		
		subnets = binary_compinations(subnets_bits)

		network = 1
		for every_subnet in subnets:
			network_addr = every_subnet + host_bits * '0'
			network_addr = str(int(network_addr[0:8], 2)) + '.' + str(int(network_addr[8:16], 2)) + '.' + str(int(network_addr[16:24], 2))
			network_addr = ip_start + network_addr
			
			fu_ip  = network_addr.split('.')[0] + '.' + network_addr.split('.')[1] + '.'
			fu_ip += network_addr.split('.')[2] + '.' + str(int(network_addr.split('.')[-1]) +1)
			
			broadcast_addr = every_subnet + host_bits * '1'
			broadcast_addr = str(int(broadcast_addr[0:8], 2)) + '.' + str(int(broadcast_addr[8:16], 2))+ '.' + str(int(broadcast_addr[16:24], 2))
			broadcast_addr = ip_start + broadcast_addr
			
			lu_ip  = broadcast_addr.split('.')[0] + '.' + broadcast_addr.split('.')[1] + '.'
			lu_ip += broadcast_addr.split('.')[2] + '.' + str(int(broadcast_addr.split('.')[-1]) -1)
			
			print("N: ", network, sep='') 
			print('Network Address: ', network_addr, sep='')
			print('First Usable: ', fu_ip, sep='')
			print('Last Usable: ', lu_ip, sep='')
			print('Broadcast Address: ', broadcast_addr, sep='')
			network += 1
			print('######\n')

	# Class B Calculations
	elif ip_class == 'B':
		ip_start = octets[0] + '.' + octets[1] + '.'
		subnets_bits = subnet - 16
		host_bits = 16 - subnets_bits
		
		subnets = binary_compinations(subnets_bits)

		network = 1
		for every_subnet in subnets:
			network_addr = every_subnet + host_bits * '0'
			network_addr = str(int(network_addr[0:8], 2)) + '.' + str(int(network_addr[8:16], 2))
			network_addr = ip_start + network_addr
			
			fu_ip  = network_addr.split('.')[0] + '.' + network_addr.split('.')[1] + '.'
			fu_ip += network_addr.split('.')[2] + '.' + str(int(network_addr.split('.')[-1]) +1)
			
			broadcast_addr = every_subnet + host_bits * '1'
			broadcast_addr = str(int(broadcast_addr[0:8], 2)) + '.' + str(int(broadcast_addr[8:16], 2))
			broadcast_addr = ip_start + broadcast_addr
			
			lu_ip  = broadcast_addr.split('.')[0] + '.' + broadcast_addr.split('.')[1] + '.'
			lu_ip += broadcast_addr.split('.')[2] + '.' + str(int(broadcast_addr.split('.')[-1]) -1)
			
			print("N: ", network, sep='') 
			print('Network Address: ', network_addr, sep='')
			print('First Usable: ', fu_ip, sep='')
			print('Last Usable: ', lu_ip, sep='')
			print('Broadcast Address: ', broadcast_addr, sep='')
			network += 1
			print('######\n')

	# Class C Calculations
	elif ip_class == 'C':
		ip_start = octets[0] + '.' + octets[1] + '.' + octets[2] + '.'
		subnets_bits = subnet - 24
		host_bits = 8 - subnets_bits
		
		subnets = binary_compinations(subnets_bits)
		
		network = 1
		for every_subnet in subnets:
			network_addr = int(every_subnet + host_bits * '0', 2)
			broadcast_addr = int(every_subnet + host_bits * '1', 2)
			print("N: ", network, sep='') 
			print('Network Address: ', ip_start, network_addr, sep='')
			print('First Usable: ', ip_start, network_addr+1, sep='')
			print('Last Usable: ', ip_start, broadcast_addr-1, sep='')
			print('Broadcast Address: ', ip_start, broadcast_addr, sep='')
			network += 1
			print('######\n')

#.#.#.

while True:
	# Get the IP from the user
	ip = input('IP: ')
	os.system('clear')
	print(ip)
	calculate_subnets(ip)

