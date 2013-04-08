class CB(object):

	def __init__(self, size):
		self.size = size
		self.buffer_list = [''] * size
		self.oldest_index = -1
		self.youngest_index = -1
		self.last_index = size - 1
		self.num_elements_in_buff = 0

	def increment_buff_size(self):
		if self.num_elements_in_buff == self.size:
			self.num_elements_in_buff = self.num_elements_in_buff
		else:
			self.num_elements_in_buff += 1

	def decrement_buff_size(self):
		if self.num_elements_in_buff == 0:
			self.num_elements_in_buff = 0
		else:
			self.num_elements_in_buff -= 1

	def increment_index(self, index):
		if index == self.size - 1:
			return 0
		else:
			return (index + 1)

	def update_indexes(self, action, index_of_action):

		if action == 'append':
			self.youngest_index = index_of_action
			if self.youngest_index == self.oldest_index:
				self.oldest_index = self.increment_index(self.oldest_index)
			elif self.oldest_index == -1:
				self.oldest_index = self.increment_index(self.oldest_index)
			self.increment_buff_size()

		elif action == 'remove':
			self.decrement_buff_size()
			if self.num_elements_in_buff == 0:
				self.youngest_index = -1
				self.oldest_index = -1
			else:
				self.oldest_index = self.increment_index(self.oldest_index)

	def list_elements(self):
		list_index = self.oldest_index
		for n in range(self.num_elements_in_buff):
			print self.buffer_list[list_index]
			list_index = self.increment_index(list_index)


	def remove_elements(self, n):
		if n > self.num_elements_in_buff:
			n = self.num_elements_in_buff

		for i in range(n):
			self.buffer_list[self.oldest_index] = ''
			self.update_indexes('remove', self.oldest_index)
			print self.buffer_list, ' youngest_index: ' + str(self.youngest_index) + ' oldest_index: ' + str(self.oldest_index) + ' num elements: ' + str(self.num_elements_in_buff)

	def append(self, n):
		while n > 0:
			element = raw_input()
			next_index = self.increment_index(self.youngest_index)
			self.buffer_list[next_index] = element
			self.update_indexes('append', next_index)
			print self.buffer_list, ' youngest_index: ' + str(self.youngest_index) + ' oldest_index: ' + str(self.oldest_index) + ' num elements: ' + str(self.num_elements_in_buff)
			n -=1



