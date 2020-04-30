def stringComprress(givenStr):
    afterCompression = ''
    charCount = 1
    for char in range(1, len(givenStr)):
        if givenStr[char-1] == givenStr[char]:
            charCount += 1
        else:
            afterCompression = afterCompression + str(charCount) + givenStr[char-1]
            charCount = 1
    try:
        afterCompression = afterCompression + str(charCount) + givenStr[char]
    except:
        afterCompression = afterCompression + str(charCount) + givenStr
    return(afterCompression)

if __name__ == "__main__":
    rawString = str(input('Enter the string: '))
    compressed = stringComprress(rawString)
    print(compressed)