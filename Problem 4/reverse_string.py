"""
Complete the following python code to reverse the string entered by the user.

Name: Christine Parrish
Lab Time: 3:00 PM Friday
"""

def reverse_string():   
    while True:
        inputString = input()
        if inputString == "Done":
            break
        elif inputString == "done":
            break
        elif inputString == "d":
            break

        else:
            i = 0
            letter = len(inputString)
            reverseString = ''

            for letter in inputString:
                reverseString += inputString[(-1 - i)]
                i += 1
            print(reverseString)
        
reverse_string()