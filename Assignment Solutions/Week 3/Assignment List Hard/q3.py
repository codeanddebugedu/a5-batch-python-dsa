"""
Write a python program to check if the list contains three consecutive common numbers in Python.

Time Complexity - O(n)
Because we are iterating only once.

Space Complexity - O(1)
"""

from typing import List


def isConsecutive(my_list: List[int]) -> None:
    flag = False
    for i in range(0, len(my_list) - 2):
        if my_list[i] == my_list[i + 1] == my_list[i + 2]:
            flag = True
            print(my_list[i])
    if flag == False:
        print("No")


isConsecutive([1, 2, 3, 4, 55, 55, 55, 6, 7, 7, 7])
isConsecutive([1, 2, 3, 4, 55, 55, 6, 7, 7])
