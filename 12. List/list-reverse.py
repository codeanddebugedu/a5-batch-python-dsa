# Time Complexity -> O(n/2)
# Space Complexity -> O(1)
# Pointers


def reverse_list(lst, left, right):
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1


my_list = [56, 43, 12, 45, 62, 41, 16, 97, 34]
n = len(my_list)

reverse_list(my_list, 0, n - 1)
# reverse_list(my_list, 0, n - 1)

print(my_list)
