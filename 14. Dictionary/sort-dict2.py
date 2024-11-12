nums = [5, 4, 4, 4, 5, 6, 7, 1, 1, 1, 6, 9, 9, 6, 1, 1, 6]


freq_map = {}
n = len(nums)
for i in range(0, n):
    if nums[i] in freq_map:
        freq_map[nums[i]] = freq_map[nums[i]] + 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)  # {5: 2, 4: 3, 6: 4, 7: 1, 1: 5, 9: 2}


print(dict(sorted(freq_map.items(), key=lambda x: x[1])))
