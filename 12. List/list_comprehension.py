# List Comprehension
# To make a new List


# nums = []
# for i in range(1, 21):
#     nums.append(i)

# nums = [i for i in range(1, 21)]
# p1
# nums = [i for i in range(1, 21) if i % 2 == 0]  # When


# p2
# nums = ["even" if i % 2 == 0 else "odd" for i in range(1, 21)]  # What to add


# p1 and p2
nums = ["even" if i % 2 == 0 else "odd" for i in range(1, 21) if i % 5 == 0]
print(nums)


# [0,0,0,0,0]
# r = [0 for i in range(1, 11)]
# print(r)
