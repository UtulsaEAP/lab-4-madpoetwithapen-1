"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Christine Parrish
Lab Time: 3:00 PM Friday
"""

def norm():
    # Write your code here

    num_values=int(input())
   
 
   
# Read the floating-point values
    values = [float(input()) for_in range(num_values)]
   

# Find the largest value
   
    max_value= max(values)
   
 
   
# Normalize each value by dividing it by the largest value
   
    normalized_values = [value/max_value for value in values]
   
 
   
# Print the normalized values with two decimal places
   
    for normalized_value in normalized_values:
       
        print(f'{normalized_value:.2f}')




if __name__ == "__main__":
    norm()