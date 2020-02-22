import re
class Palindrome:
    def text(self, set_of_chars):
        set_of_chars = re.sub('[^A-Za-z0-9]+','',set_of_chars).lower()
        print(set_of_chars == set_of_chars[len(set_of_chars)::-1])
        
if __name__ == '__main__':
    cObj = Palindrome()
    cObj.text(str(input()))
