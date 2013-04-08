top_four = []

def do_element(element):
	if len(top_four) == 0:
		top_four.append(element)
	
	else:
		temp = element
		for i, el in enumerate(top_four):
			''' search for one where element element is greater, put that one in temp element, and use that from then on -- sorted list in decreasing order '''
			if temp > el:
				top_four[i] = temp
				temp = el
		if len(top_four) < 4:
			top_four.append(temp)

def grab_inputs():
	n = int(raw_input())
	for i in range(n):
		el = int(raw_input())
		do_element(el)
	for el in top_four:
		print el

grab_inputs()
