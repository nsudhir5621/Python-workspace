# Hacker Rank Problems


# Python: Exceptions
# Problem: Catch division errors
# Link: https://www.hackerrank.com/challenges/exceptions/problem
# for i in range(int(input())):
#     try:
#         a, b = map(int, input().split())
#         print(a // b)
#     except ZeroDivisionError:
#         print("Error Code: integer division or modulo by zero")
#     except ValueError as e:
#         print("Error Code:", e)


# Python: Incorrect Regex
# Problem: Validate regex pattern
# Link: https://www.hackerrank.com/challenges/incorrect-regex/problem
# import re
# for _ in range(int(input())):
#     try:
#         re.compile(input())
#         print(True)
#     except re.error:
#         print(False)
# Notes: Used re.error to catch invalid regex
