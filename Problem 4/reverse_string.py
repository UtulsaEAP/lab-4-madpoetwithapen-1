"""
Complete the following python code to reverse the string entered by the user.

Name: Christine Parrish
Lab Time: 3:00 PM Friday
"""

def reverse_string():  
    while True:
        user_input = input()
        if user_input.lower()in["done","d"]: 
            break   
    reversed_text = user_input[::-1]
    print(reversed_text)

if __name__ == "__main__": 
    reverse_string()
