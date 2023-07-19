'''lucas testing'''

nums = [5,70,812,4,2,8,91,54,812]
print(nums)
print("WHILE")
i = 0

while i < len(nums):
    num = nums[i]
    if nums[i] < 10:
        print("Menor")
    else:
        print("Maior")
    if num == 812:
        print("wow")
    i = i +1

print("FOR")

for num in nums:
    if num < 10:
        print("Menor")
    else:
        print("Maior")
    if num == 812:
        print("wow")
