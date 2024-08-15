letter = '''  Dear <|Name|>, 
\tYou are selected! 
<|Date|> ''' 

name = input("Enter a name: ")
date = input("Enter date: ")

print(letter.replace("<|Name|>", name).replace("<|Date|>", date))