terms = dict()
reverse_terms = dict()
tuples = []
sorted_list = []

def add_term(term):
	terms[term] = terms.get(term, 0) + 1

def invert_dict(d):
	'''takes in a dictionary, and swaps the values and keys '''
	for key in d:
		val = d[key]
		if val not in reverse_terms:
			reverse_terms[val] = [key]
		else:
			reverse_terms[val].append(key)

def build_tuples(dict):
	for key, val in dict.items():
		val.sort()
		tup = (key, val)
		tuples.append(tup)
	tuples.sort(reverse = True)

def grab_inputs():
	n = int(raw_input())
	for i in range(n):
		term = raw_input()
		add_term(term)
	invert_dict(terms)
	build_tuples(reverse_terms)
	for i, lst in tuples:
		sorted_list.extend(lst)
	n = int(raw_input())
	for i in range(n):
		print sorted_list[i]
	

grab_inputs()