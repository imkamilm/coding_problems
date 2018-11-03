# Daily Coding Problem
#----------------------
# Good morning! Here is your coding interview problem for today.
#
# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

def new_array(A):
    N = len(A)

    new_A = [1] * N
    for i in range(N):
        for n in range(N):
            if n == i: continue
            new_A[i] *= A[n % N]

    return new_A

# Follow-up: what if you can't use division?

def new_array_2(A):
    N = len(A)

    new_A = [1] * N
    for i in range(N):
        for n in range(N):
            if n == i: continue
            new_A[i] *= A[n + 1 - i]

    return new_A


a = [1,2,3,4,5]
print(new_array(a))
print(new_array(a))
