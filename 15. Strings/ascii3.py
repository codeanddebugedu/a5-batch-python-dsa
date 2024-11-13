def isAllDigit(s: str) -> bool:
    n = len(s)
    for i in range(0, n):
        ascii_value = ord(s[i])
        if ascii_value > 57 or ascii_value < 48:
            return False
    return True


user_string = input("Enter a string = ")
print(isAllDigit(user_string))
