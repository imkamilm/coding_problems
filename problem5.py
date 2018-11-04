# Daily Coding Problem
# --------------------------
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Stripe.
#
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

def lowest_positive_num(A):
    s = list(set(list(filter(lambda x: x >= 0, sorted(A)))))
    
    missing_num = -1
    for i in range(len(s) - 1):
        if s[i] + 1 != s[i+1]:
            missing_num = s[i] + 1
    
    return missing_num if missing_num != -1 else s[len(s) - 1] + 1 

a = [3,4,-1,1]
print(lowest_positive_num(a))
