n = int(input("Write the number of elements of the Fibonacci sequence: "))
fib = [0, 1] # tab keeps elements of the Fibonacci sequence

i = 0 # used to
while (i<n-2): # we have 2 first elements in tab fib - that's why we deduct 2 from n
    nextElement = fib[i] + fib[i+1] # counts next element
    fib.append(nextElement) # increases tab
    i = i+1

print(fib)