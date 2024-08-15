text = input("Enter text: ")

def vowel_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count
    
print(vowel_count(text))