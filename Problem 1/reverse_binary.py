"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Christine Parrish
Lab Time: 3:00 PM Friday 

"""
def reverse_binary():
    x = int(input())
    binary_string = ""


    while x > 0:
        binary_string += str(x % 2)
        x //= 2
    print(binary_string)
    #print(binary_string[::-1])


if __name__ == "__main__":
    reverse_binary()
