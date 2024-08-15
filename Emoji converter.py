print('''
1. ":)" = happy
2. ":(" = sad
3. ":-/" = confuse
4. ":@" = angry
5. ":o" = surprise
6. ":x" = love
''')

def emoji_converter(message):
    words =message.split(" ")
    emojies ={
        ":)" : "😊",
        ":(" : "😔",
        ":-/" : "🤔",
        ":@" : "😡",
        ":o" : "😲",
        ":x" : "😘"
    }

    output = ""
    for word in words:
        output += emojies.get(word, word) + " "
        return output
message = input("> ")
result = emoji_converter(message)
print(result)