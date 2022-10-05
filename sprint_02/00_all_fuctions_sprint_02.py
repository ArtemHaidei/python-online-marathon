#test 1
# def double_string(data):
# 	counter = []

# 	for x in range(len(data)):
# 		chek_list = []

# 		for i in range(len(data)):
# 			item = data[x] + data[i]

# 			if item in data and item not in chek_list:
# 				chek_list.append(item)
# 		counter += chek_list

# 	return len(counter)


#test 2
# def morse_number(str_num):
# 	result = []
# 	for x in str_num:
# 		if int(x) <= 5:
# 			result.append('-----'.replace('-', '.', int(x)))
# 		else:
# 			result.append('-----'.replace('-', '.',10 - int(x))[::-1])

# 	return ' '.join(result)


#test 3
# def vectors_length(x1, x2, y1, y2):
# 	return (((x2 - x1) ** 2) + ((y2 - y1)) ** 2) ** 0.5


# def figure_perimetr(string):
# 	#order - LB, LT, RT, RB
# 	vectors = {x[0:2]: (int(x[-3]), int(x[-1])) for x in string[1:].split("#")}

# 	v1 = vectors_length(vectors['LB'][0], vectors['LT'][0], vectors['LB'][1], vectors['LT'][1])
# 	v2 = vectors_length(vectors['LT'][0], vectors['RT'][0], vectors['LT'][1], vectors['RT'][1])
# 	v3 = vectors_length(vectors['RT'][0], vectors['RB'][0], vectors['RT'][1], vectors['RB'][1])
# 	v4 = vectors_length(vectors['RB'][0], vectors['LB'][0], vectors['RB'][1], vectors['LB'][1])

# 	return sum([v1, v2, v3, v4])


#test 4
# import re


# pretty_message = lambda x: re.sub(r"(\w{1,3}?)\1+", r"\1", x)


#test 5
# import re


# def max_population(lst):
    
#     sorted_lst = [re.findall(r"((?:eu|af|me)_[^,]+|\d{5})", x) for x in lst]
#     int_lst = sorted([(x[0], int(x[1])) for x in sorted_lst[1:]], key=lambda x: x[1])

#     return int_lst[-1]
