# As input data you have list of strings with information about some location:

# "id,name,poppulation,is_capital",
# "3024,eu_kyiv,24834,y",
# "3025,eu_volynia,20231,n",
# "3026,eu_galych,23745,n",
# "4892,me_medina,18038,n",
# "4401,af_cairo,18946,y",
# "4700,me_tabriz,13421,n",
# "4899,me_bagdad,22723,y",
# "6600,af_zulu,09720,n"

# Using regular expression write method max_population() for 
# parsing strings and get info about location with highest population 


import re


def max_population(lst):
    
    sorted_lst = [re.findall(r"((?:eu|af|me)_[^,]+|\d{5})", x) for x in lst]
    int_lst = sorted([(x[0], int(x[1])) for x in sorted_lst[1:]], key=lambda x: x[1])

    return int_lst[-1]


data = ["id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"]

print(max_population(data))