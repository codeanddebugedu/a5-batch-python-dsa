def is_prime(num):
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


nums = [5, 6, 4, 3, 2, 19, 7, 55, 81, 87]

n = len(nums)
for i in range(0, n):
    if is_prime(nums[i]) == True:
        print(nums[i], end=" ")
