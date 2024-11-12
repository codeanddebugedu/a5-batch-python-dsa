nums = [5, 4, 4, 4, 5, 6, 7, 1, 1, 1, 6, 9, 9, 6, 1, 1, 6]


freq_map = {}

# for num in nums:
#     if num in freq_map:
#         freq_map[num] = freq_map[num] + 1
#     else:
#         freq_map[num] = 1


n = len(nums)
for i in range(0, n):
    if nums[i] in freq_map:
        freq_map[nums[i]] = freq_map[nums[i]] + 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)
