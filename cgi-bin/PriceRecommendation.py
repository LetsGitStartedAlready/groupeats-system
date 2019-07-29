inputFile = open("PriceTestData.txt")
lines = inputFile.readlines()
prices = []
for line in lines:
    prices.append(int(line.strip()))
prices.sort()
def aboveAverageCount(array):
    average = sum(prices)/len(prices)
    count = 0
    for price in prices:
        if (price > average):
            count+=1
    return count
aboveCount = aboveAverageCount(prices)
percentAboveAverage = aboveCount/len(prices)
ignoreCount = min(int(1/percentAboveAverage),aboveCount)
print(ignoreCount)
while ignoreCount > 0:
    del prices[len(prices)-1]
    ignoreCount -= 1
print("Best price match is: " + str(sum(prices)/len(prices)))