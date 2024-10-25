nums = [-5000, -60000, -400000, -300000, -20000, -100000, -780000, -650000]


#
#
maxi = float("-inf")
n = len(nums)

for i in range(0, n):
    maxi = max(maxi, nums[i])

print(maxi)


# for i in range(0, n):
#     if nums[i] > maxi:
#         maxi = nums[i]
