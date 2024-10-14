#1. Sum and Average of List Elements
#Write a function that takes a list of numbers 
# as input and returns both the sum and average 
# of the elements in the list.
input = [5, 10, 15, 20, 25]

#time complexity is big o(n)
def sum_average(nums: list[int]):
    #big o(1)
    length = len(nums)
    sum = 0

    #big o(n)
    for i in nums:
        #big o(1)
        sum += i

    #big o(1)
    average = sum / length

    return "the average is {0} and the sum is {1}".format(average, sum)

print(sum_average(input))