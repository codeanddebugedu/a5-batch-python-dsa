# in / not in O(N)


def find_the_element(lst, num):
    # if num in lst:
    #     return True
    # return False
    n = len(lst)
    for i in range(0, n):
        if num == lst[i]:
            return True
    return False


nums = [5, 6, 4, 3, 2, 19, 7, 55, 81, 87]
user_input = int(input("Enter a number = "))

print(find_the_element(nums, user_input))
