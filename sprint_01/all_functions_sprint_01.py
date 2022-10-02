# test 1
def kthTerm(n, k):
    list_ = [1, n**1, n**1 + 1]
    for x in range(2, 31):
        size_list = len(list_)
        number_square = n ** x
        list_.append(number_square)
        for i in range(size_list):
            if len(list_) > 100:
                break
            list_.append(list_[i] + number_square)

    return list_[k - 1]


# test 2
# def filterBible(scripture, book, chapter):
#     return [x for x in scripture if x[0:2] == book and x[2:5] == chapter]


# test 3
def isPalindrome(str):
    if len(str) <= 3:
        return True

    str_part1 = str[:len(str) // 2]
    str_part2 = str[(-len(str) // 2) + 1:] \
        if len(str) % 2 != 0 else str[(-len(str) // 2):]

    return True if str_part1 == str_part2 \
                   or str_part1 == str_part2[::-1] else False




# test 4
# def findPermutation(p, q):
#     return [i + 1 for x in range(len(q)) for i in range(len(p)) if q[x] == p[i]]


# test 5
# def toPostFixExpression(tokenlist):
#     items = {'%': 3, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
#     result = []
#     postfixlist = []

#     for token in tokenlist:
#         if token.isdigit():
#             postfixlist.append(token)

#         elif token == '(':
#             result.append(token)
#         elif token == ')':
#             topToken = result.pop()
#             while topToken != '(':
#                 postfixlist.append(topToken)
#                 topToken = result.pop()
#         else:
#             while (not result == []) and \
#                     (items[result[-1]] >= items[token]):
#                 postfixlist.append(result.pop())
#             result.append(token)

#     while not result == []:
#         postfixlist.append(result.pop())
#     return postfixlist



# test 6
# def order(a):
#     if a == sorted(a):
#         return "ascending"
#     elif a == sorted(a, reverse=True):
#         return "descending"
#     else:
#         return "not sorted"


# test 7
# def Cipher_Zeroes(N):
#     points = sum([1 for x in N if x in '069'] + [2 for i in N if i == '8'])
#     if points == 0:
#         return '{0:b}'.format(points)
#     points += -1 if points % 2 == 0 else 1
#     return '{0:b}'.format(points)


# test 8
# def studying_hours(a):
#     result, check = [], []
#     index_ = 0
#     while len(a) != index_:
#         if index_ + 1 < len(a) and a[index_ + 1] >= a[index_]:
#             check.append(a[index_])
#         elif len(result) <= len(check):
#             if check[-1] <= a[index_] or index_ == len(a) - 1 and result[-1] <= a[index_]:
#                 check.append(a[index_])
#             result = check
#             check = []
#         else:
#             check = []
#         index_ += 1

#     return len(result)

