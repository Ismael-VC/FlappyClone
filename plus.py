"""
e.g.:
sum_double(1, 2) -> 3
sum_double(3, 2) -> 5
sum_double(2, 2) -> 8
Made by Dj_System
"""

#input
n1 = int(raw_input('Enter an integer: '))
n2 = int(raw_input('Enter an integer: '))

#process
def sum_double(a, b):
    if a != b:
        return a+b
    else:
        return 2*(a+b)

#output
print 'The result is: ' + str(sum_double(n1, n2))
