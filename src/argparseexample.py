import argparse

# Declaring a parser
parser = argparse.ArgumentParser()

# Add arguments to parser
parser.add_argument('-firstname', "--firstname", help="Your first name")
parser.add_argument('-lastname', "--lastname", help="Your last name") 

# Get the value of the args
args = parser.parse_args()

# Read the value and perform operation
opts = args.firstname +" "+ args.lastname

# Print the result
print("Your full name: ",opts)