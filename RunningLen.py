# Function that gets a string as an parameter
def stringComprress(givenStr):
    # Initializing an empty string, it hold the compressed string output from the loop
    afterCompression = ''
    # Assuming there is at least one character in the given string
    charCount = 1
    # Looping through all the charecters in the given string
    # String with index 1 through the length of the given string
    for char in range(1, len(givenStr)):
        # Condition to check if the current string is same as previous string
        if givenStr[char-1] == givenStr[char]:
            # If the current charecter is same as the previous charecter?, variable charCount will increment by 1
            charCount += 1
        # Else condition. If the given charecter is not same as the previous charecter
        else:
            # Variable afterCompression is concatenated with the variable charCount and the previous charecter
            afterCompression = afterCompression + str(charCount) + givenStr[char-1]
            # Reetting the variable charCount as we have reached the end of similar characters
            charCount = 1
    # Within the above for loop, the last set of similar charecters are skipped because the else condition will not be satisfied
    # Try block will make sure to add charCount and the current charecter to the string variable afterCompression
    try:
        afterCompression = afterCompression + str(charCount) + givenStr[char]
    # Except block will handle Border case inputs; If there is only one charecter in the given string
    except:
        afterCompression = afterCompression + str(charCount) + givenStr
    # Return afterCompression to the calling function
    return(afterCompression)

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