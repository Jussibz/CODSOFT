import random 
import string

while True:
    try:
        length = int(input("Enter the desired length of the password."))
        if length <= 0:
            print("Please enter a positive integer for the length. ")
            continue
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        print("Generated Password: ", password)
        break
    except ValueError:
        print("Please enter a valid integer for the length. ")