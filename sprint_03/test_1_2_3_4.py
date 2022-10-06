#test 1
# def outer(name):
#     def inner():
#         print(f'Hello, {name}')
    
#     return inner


# outer("Tom")()



#test 2
#def create(string1): return lambda string2: string1 == string2
 

#test 3

# import string


# letters_and_digits = string.ascii_lowercase + string.digits + '@._'


# def create_account(user_name, password, secret_words):
#     def chek():
#         flag = False

#         if not set(password) <= set(letters_and_digits) or not any([x.islower() for x in password]) or not len(password) >= 6 \
#                 or not any([[x.isupper() for x in password]]) or not any([x in string.digits for x in password]):
#                 flag = Ture



        

#     return check



# tom = create_account("Tom", "Qwerty1_", ["1", "word"])  
# check1 = tom("Qwerty1_",  ["1", "word"]) 
# check2 = tom("Qwerty1_",  ["word"]) 
# check3 = tom("Qwerty1_",  ["word", "2"]) 
# check4 = tom("Qwerty1!",  ["word", "12"]) 



#test 4
def divisor(n):
    def inner():
        lst = [x for x in range(1, n + 1) if n % x == 0]



three = divisor(3)
print(next(three))
print(next(three))
print(next(three))












