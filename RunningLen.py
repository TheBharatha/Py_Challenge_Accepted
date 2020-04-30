# Function that gets a string as an parameter
def stringComprress(givenStr):
    # Initializing an empty string, it hold the compressed string output from the loop
    encoded = ''
    # Assuming there is at least one character in the given string
    charCount = 1
    # Looping through all the characters in the given string
    # String with index 1 through the length of the given string
    for char in range(1, len(givenStr)):
        # Condition to check if the current string is same as previous string
        if givenStr[char-1] == givenStr[char]:
            # If the current character is same as the previous character?, variable charCount will increment by 1
            charCount += 1
        # Else condition. If the given character is not same as the previous character
        else:
            # Variable afterCompression is concatenated with the variable charCount and the previous character
            encoded = encoded + str(charCount) + givenStr[char-1]
            # Resetting the variable charCount as we have reached the end of similar characters
            charCount = 1
    # Within the above for loop, the last set of similar characters are skipped because the else condition is not satisfied
    # Try block will make sure to add charCount and the current character to the string variable afterCompression
    try:
        encoded = encoded + str(charCount) + givenStr[char]
    # Except block will handle Border case inputs; If there is only one character in the given string
    except:
        encoded = encoded + str(charCount) + givenStr
    # Return afterCompression to the calling function
    return(encoded)

# Driver code
if __name__ == "__main__":
    # Prompts for input. The input is converted to a string
    rawString = str(input('Enter the string: '))
    if rawString != '':
        # rawString is passed as an argument to the function stringComprress()
        compressed = stringComprress(rawString)
    else:
        compressed = 'The string is empty!'
    # Prints the returned compressed string
    print(compressed)