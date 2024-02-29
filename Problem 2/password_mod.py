"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Christine Parrish
Lab Time: 3:00 PM Friday
"""

def password_mod():
    word = input()
    password = ''
    letter = len(word)
    target = 0
    for letter in word:
        if word[target] == 'i': 
            password += '1'
            target += 1
        elif word[target] == 'a':
            password += '@'
            target += 1
        elif word[target] == 'm':
            password += 'M'
            target += 1
        elif word[target] == 'B':
            password += '8'
            target += 1
        elif word[target] == 's':
            password += '$'
            target += 1
        else:
            password += word[target] 
            target += 1

    password += '!'

    print(password)


if __name__ == "__main__":
    password_mod()