from Circular_Buffer import CB

def grab_inputs():
	n = int(raw_input())
	if ((n < 0) or (n>10000)):
		print "size out of range"
		return False
	else:	
		buff = CB(n)
		#print buff.print_buff()
	
		command = ''

		while command != 'Q':
			command = raw_input()
			command_list = command.split()
			if command_list[0] == 'A':
				buff.append(int(command_list[1]))
			if command_list[0] == 'L':
				buff.list_elements()
			if command_list[0] == 'R':
				buff.remove_elements(int(command_list[1]))
			elif command_list[0] == 'H':
				print 'A n - append the following n lines to the buffer.'
				print 'R n - remove the first n elements of the buffer.'
				print 'L - list the buffer'
				print 'Q - Quit'

grab_inputs()