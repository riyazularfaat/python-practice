import random
secret_number = random.randint (0, 10)
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    
    if guess == secret_number:
        print ("You won!")
        break
else: #in Python, we can use else section for while loop
    print("Sorry, try again next time....")