import string
import random
 
 
# store all characters in lists
lowercase_set = list(string.ascii_lowercase)  # Lowercase character set
uppercase_set = list(string.ascii_uppercase)  # Uppercase character set
digit_set = list(string.digits)    # Digit set
punc_set = list(string.punctuation)  # Special character set
 
# Function to generate password
def generate_password(numOFnum, numOFchar):
    
    # shuffle all lists
    random.shuffle(lowercase_set)
    random.shuffle(uppercase_set)
    random.shuffle(digit_set)
    random.shuffle(punc_set)
    
    result = []  # Holds the result
    flag = 0
    
    for x in range(int(numOFchar)):
        if flag == 1:
            result.append(lowercase_set[x])
            flag = 0
        else :
            result.append(uppercase_set[x])
            flag = 1
    

    for x in range(int(numOFnum)):
        if flag == 1:
            result.append(digit_set[x])
            flag = 0
        else :
            result.append(punc_set[x])
            flag = 1

    
    # shuffle result to generate password
    random.shuffle(result)
     
     
    # join result
    password = "".join(result)
    return password




# Ask user about the number of characters
# pass_length = input("How many characters do you want in your password? ")
# no_of_chars = input("No of letters [ Should be less than "+ pass_length +" ] :")

# no_of_num = int(pass_length) - int(no_of_chars)

# password = generate_password(int(no_of_num), int(no_of_chars))
 

# print("Strong Password: ", password)
