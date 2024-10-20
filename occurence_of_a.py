# Function to count the occurrence of 'a'
def count_a(string):
    count = 0  # Initialize count to 0
    # Loop through each character in the string
    for char in string:
        # Check if the character is 'a'
        if char == 'a':
            count += 1  # Increment count if 'a' is found
    return count

# Taking input from the user
user_string = input("Enter a string: ")

# Calling the function and printing the result
a_count = count_a(user_string)
print(f"The occurrence of 'a' in the string is: {a_count}")
