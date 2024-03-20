"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Christine Parrish
Lab Time: 3:00 PM Friday
"""
def inc_5():
    # Get user input for the two integers
    num1 = int(input())
    num2 = int(input())


    # Check if num1 is less than or equal to num2
    if num1 <= num2:
        # Output the first integer
        print(num1, end=" ")


        # Output subsequent increments of 5 until reaching num2
        while num1 + 5 <= num2:
            num1 += 5
            print(num1, end=" ")


        # Print a newline at the end
        print()
    else:
        print("Second integer can't be less than the first.")


if __name__ == '__main__':
    inc_5()
