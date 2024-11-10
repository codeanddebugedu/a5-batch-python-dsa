# To create a list of prime numbers from 2 to 100


# 1 to 100, divisible by 2 and 7
def prime_no(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False


nums = [i for i in range(20, 41) if prime_no(i)]
print(nums)
