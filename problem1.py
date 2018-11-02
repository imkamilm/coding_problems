# Daily Problem 



# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def adds_up(nums, k):
    for i in range(len(nums)):
        for n in range(i+1, len(nums)):
            if nums[i] + nums[n] == k:
                return True
    return False

print(adds_up([10,15,3,7,21,3,5], 8))
