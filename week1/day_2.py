# Hacker Rank Problems

# Python: Loops
# Problem: Print squares of 0 to n-1
# Link: https://www.hackerrank.com/challenges/python-loops/problem
# n = int(input())  # Get input n
# for i in range(n):
#     print(i * i)  # Print square
# Notes: Used range(n) for iteration, converted input to int


# Python: List Comprehensions
# Problem: Generate coordinates where sum != n
# Link: https://www.hackerrank.com/challenges/list-comprehensions/problem
# x, y, z, n = [int(input()) for _ in range(4)]  # Get inputs
# print([[i, j, k] for i in range(x+1) # +1 is added since the end of range is excluded by default
#                  for j in range(y+1)
#                  for k in range(z+1)
#                  if i+j+k != n])
# Notes: Nested loops in one line, tested with x=1, y=1, z=1, n=2


# Python: Lists
# Problem: Perform list operations (insert, remove, etc.)
# Link: https://www.hackerrank.com/challenges/python-lists/problem
# N = int(input())  # Number of commands
# L = []
# for _ in range(N):
#     cmd = input().split()
#     if cmd[0] == "insert":
#         L.insert(int(cmd[1]), int(cmd[2]))
#     elif cmd[0] == "print":
#         print(L)
#     elif cmd[0] == "remove":
#         L.remove(int(cmd[1]))
#     elif cmd[0] == "append":
#         L.append(int(cmd[1]))
#     elif cmd[0] == "sort":
#         L.sort()
#     elif cmd[0] == "pop":
#         L.pop()
#     elif cmd[0] == "reverse":
#         L.reverse()
# Notes: Handled multiple commands, used conditionals for logic
