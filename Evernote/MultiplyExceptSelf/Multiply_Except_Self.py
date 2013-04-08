input_list = []
result_list = []


def grab_inputs():
	n = int(raw_input())
	result_list = [1] * n
	for i in range(n):
		element = int(raw_input())
		for x in range(n):
			if x != i:
				result_list[x] = result_list[x] * element

		input_list.append(element)
	for val in result_list:
		print val

grab_inputs()