"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Christine Parrish
Lab Time: 3:00 PM Friday
"""

def norm():
    # Write your code here
    num_values=int(input())
    values = [float(input()) for _ in range(num_values)]
    max_value= max(values)
    normalized_values = [value/max_value for value in values]
    for normalized_value in normalized_values:
       
        print(f'{normalized_value:.2f}')




if __name__ == "__main__":
    norm()