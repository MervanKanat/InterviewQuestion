import random 

# Determine a random sample size
sample = random.randint(5, 20)

# List of numbers from 1 to 99
numbers_list = list(range(1, 100))

# Select 'sample' number of random elements from the list
numbers = random.sample(numbers_list, sample)
print(numbers)

# Initialize the largest and the second largest numbers to the smallest possible values
largest = float('-inf')
second_largest = float('-inf')

# Iterate through the numbers in the list to find the largest and the second largest numbers
for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number

print("The largest number:", largest)
print("The second largest number:", second_largest)
