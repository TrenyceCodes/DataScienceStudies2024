# Lists
#1 byte = 8 bits - stored in the memory address
data = [0] * 8
print(data) #length of 8 items of zero

data[2] += 1
print(data) #increments 1 to second index element

primes = [2, 3, 5, 7, 11, 13, 17, 19]
print(len(primes))
extras = [23, 29, 31]

#adds on items to list(reference not copy)
primes.extend(extras) 
print(primes)

#memory allocation
import sys
data = []
n = 26
for k in range(n):
    a  = len(data)
    
    #returns size of the list in bytes
    b = sys.getsizeof(data)
    print('Length: {0:1d}; Size in bytes: {1:2d}'.format(a, b))
    data.append(None)