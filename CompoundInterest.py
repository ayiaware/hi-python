principalSum = 1000
norminalRate = 5
compFrequency = 12
timeLength = 2

accumulatedAmount = principalSum * (pow((1 + (norminalRate / 100) / compFrequency), timeLength * compFrequency))

print("The Accumulated Amount is %.2f" % accumulatedAmount)





