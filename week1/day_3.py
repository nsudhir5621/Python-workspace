# Hacker Rank Problems

# Python: Find the runner-up score

# n = int(input("Enter n: "))
# arr = list(map(int, input("Enter numbers: ").split())) # map applies the function before the comma to an iterable after comma.
# if len(arr) != n: # to check valid input
#     print ("You must enter exactly ", n ," numbers")
# else:
#     arr = sorted(arr) # sorts array
#     unique = list(dict.fromkeys(arr)) # dict.fromkeys creates a dictionary where each sequence becomes a key with value none, In dictionary, duplicate values can exist but not duplicate keys.
#     print("Runner-up: ",unique[-2])


# Python: Write a Function
# Problem: Check if year is leap year
# Link: https://www.hackerrank.com/challenges/write-a-function/problem

# def is_leap(year):
#     leap = False
#
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         leap = True
#     return leap
# year = int(input())
# print(is_leap(year))


# Python: Nested Lists
# Problem: Sort students, print second-lowest names
# Link: https://www.hackerrank.com/challenges/nested-list/problem

# students = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     students.append([name, score])

# scores = sorted(set([s[1] for s in students]))

# second_lowest = scores[1]

# names = sorted([s[0] for s in students if s[1] == second_lowest])

# for name in names:
#     print(name)


# Python: Finding the Percentage
# Problem: Calculate average score
# Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem

# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split() # * means take the rest input, here name takes one input while *line takes remaining inputs
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()

# marks = student_marks[query_name]

# avg_scores = sum(marks) / len(marks)

# print(f"{avg_scores:.2f}") #.2f formats the float value of avg_scores to 2 decimal points
