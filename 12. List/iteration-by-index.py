nums = [67, 54, 27, 89, 98, 9999, 76]


n = len(nums)

# Iterate by Index
# for i in range(0, n):
#     print(nums[i])


for i in range(n - 1, -1, -1):
    print(nums[i], end=" ")
