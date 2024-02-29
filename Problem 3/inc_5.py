"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Christine Parrish
Lab Time: 3:00 PM Friday
"""

def inc_5(int1,int2):
    for x in range(int1, int2, 5):
        print(str(x) + ' ')    



if __name__ == '__main__':
    inc_5()