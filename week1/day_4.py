# Hacker Rank Problems


# Python: Tuples
# Problem: Create tuple, compute hash
# Link: https://www.hackerrank.com/challenges/python-tuples/problem
# n = int(input())
# integer_list = map(int, input().split())
# t = tuple(integer_list)
# print(hash(t)) #hash is a predefined in-built function
# Notes: Used tuple() to convert list, hash() for result


# Python: Introduction to Sets
# Problem: Calculate average of unique values
# Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

# def average(array):
#     distinct_heights = set(array) # Used set to avoid duplicates
#     return sum(distinct_heights) / len(distinct_heights)
# n = int(input())
# arr = list(map(int, input().split()))
# result = average(arr)
# print(result)
# Notes: Check variables before operating such as in round.


# Python: Set Mutations
# Problem: Perform set operations
# Link: https://www.hackerrank.com/challenges/py-set-mutations/problem

# length_main_set = (int(input("Enter the number of elements:\n")))
# main_set = set(map(int, input(f"\nEnter {length_main_set} space-separated values:\n").split()))
# n = int(input("\nEnter the number of operations:\n "))
#
# for _ in range(n):
#     operation = input("\nEnter the operation type and the length of next set:\n").split()
#     new_set = set(map(int, input(f"\nEnter {operation[1]} space-separated values:\n").split()))
#     if operation[0] == "update":
#         main_set.update(new_set)
#     elif operation[0] == "intersection_update":
#         main_set.intersection_update(new_set)
#     elif operation[0] == "difference_update":
#         main_set.difference_update(new_set)
#     elif operation[0] == "symmetric_difference_update":
#         main_set.symmetric_difference_update(new_set)

# main_set_total = int(sum(main_set))
# print(main_set_total)

# Notes: competitive platforms like hackerrank will throw error if we write prompt, must leave all input() and print() empty.
