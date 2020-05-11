n = int(input("Number of white balls: "))
m = int(input("Number of black balls: "))
k = int(input("Number of sampled balls: "))

ballsNumber = n + m # number of all balls
twoWhite = 1
twoBlack = 1

if n>=k:
    tmp = ballsNumber
    i = k

    while i>0:
        twoWhite *= (n/tmp)
        n -= 1
        tmp -= 1
        i -= 1

else:
    twoWhite = 0

print(twoWhite)

if m>=k:
    tmp = ballsNumber
    i = k

    while i>0:
        twoBlack *= (m/tmp)
        m -= 1
        tmp -= 1
        i -= 1

else:
    twoBlack = 0

print("Probability of 2 balls of the same color: ", twoWhite+twoBlack)

