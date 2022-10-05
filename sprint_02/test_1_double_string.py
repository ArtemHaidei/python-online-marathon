#test 1
# As input data, you have a list of strings.
# Write a method double_string() for counting the number of strings from the list,
# represented in the form of the concatenation of two strings from this arguments  list:


def double_string(data):
	counter = []

	for x in range(len(data)):
		chek_list = []

		for i in range(len(data)):
			item = data[x] + data[i]
			
			if item in data and item not in chek_list:
				chek_list.append(item)
		counter += chek_list

	return len(counter)


data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
print(double_string(data)) #3

data1 = ['aa', 'abc', 'qwerqwer']
print(double_string(data1)) #0

data2 = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
print(double_string(data2)) #3

data3 = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa']
print(double_string(data3)) #4