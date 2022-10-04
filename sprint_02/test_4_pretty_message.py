import re


pretty_message = lambda x: re.sub(r"(\w{1,3}?)\1+", r"\1", x)


data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
print(pretty_message(data))
# This is echo string. Replace repeated groups of symbols

data = "Another input data string"
print(pretty_message(data))
# Another input data string