''' This program should identify the max value wihthin the list variable '''

nums = [5,70,812,4,2,8,91,54,812,11077,3,8]

max_value = 0

for xx in nums:
    if xx > max_value:
        max_value = xx


print("this is the max value", max_value)