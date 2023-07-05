''' This program should identify, for each item from a list variable, if the item
is an even number or an odd number '''

nums = [5,70,812,4,2,8,91,54,812,11077,3,8]
even_numbers = []
odd_numbers = []

for num in nums:
    if num % 2 == 0:
        even_numbers.append(num)

    else:
        odd_numbers.append(num)

print("Even Numbers: ")
print(even_numbers)

print("Odd Numbers: ")
print(odd_numbers)