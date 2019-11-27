#The function max() and max_of_three() from previous exercises will only work for two and three numbers,
# respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance
# how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.

def max_in_list(*numbers):
    s = [i for i in numbers]
    s.sort(reverse=True)
    return s[0]
