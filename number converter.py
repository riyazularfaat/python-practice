def number_converter(phone):
    digits = {
        "0" : "Zero",
        "1" : "One",
         "2" : "Two",
         "3" : "Three",
         "4" : "Four",
         "5" : "Five",
         "6" : "Six",
         "7" : "Seven",
         "8" : "Eight",
         "9" : "Nine",
         "-" : "Minus",
         "+" : "Plus"
    }
    
    output = "" 
    for ch in phone:
        output += digits.get(ch) + " "
    return output

phone = input("Phone: ") 
result = number_converter(phone)
print(result)
