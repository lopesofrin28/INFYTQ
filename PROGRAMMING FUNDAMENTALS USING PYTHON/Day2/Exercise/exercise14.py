# A teacher in a school wants to find and display the grade of a student based on his/her percentage score.
# The criterion for grades is as given below:
#
#                     Score (both inclusive)	Grade
#                     Between 80 and 100	      A
#                     Between 73 and 79	      B
#                     Between 65 and 72	      C
#                     Between 0 and 64	      D
#                     Any other value           Z
#
# Assume that the percentage score is a whole number.
# Write a python program for the above requirement. Identify the test data and use it to test the program.
#



#PF-Tryout
#Start writing your code here
def score(marks):
    if marks>=80 and marks<=100:
        grade="A"
    elif marks>=73 and marks<=79:
        grade="B"
    elif marks>=65 and marks<=72:
        grade="C"
    elif marks>=0 and marks<=64:
        grade="D"
    else:
        grade="Z"

    return grade


grade=score(-20)
print(grade)
