import operator
def buildWeightArray(input, weightNum):
    firstInput = input
    weights = []
    weights.append(input)
    input -= 1
    while (input > 0):
        if (weightNum < firstInput):
            weights[0] += input
            weightNum += 1
            input -= 1
        else:
            weights.append(input)
            input -=1
    return weights
cuisineNum = 9
inputFile = open("CuisineTestData.txt")
lines = inputFile.readlines()
goodcuisines = {}
badcuisines = {}
for x in range(len(lines)):
    if (x%3==1): 
        line = lines[x].split()
        weights = buildWeightArray(cuisineNum/3, len(line))
        i = 0
        for cuisine in line:
            if cuisine in goodcuisines:
                goodcuisines[cuisine] += weights[i] + 1
            else:
                goodcuisines[cuisine] = weights[i]
            i+=1
    if (x%3==2):
        line = lines[x].split()
        weights = buildWeightArray(cuisineNum/3, len(line))
        i = 0
        for cuisine in line:
            if cuisine in badcuisines:
                badcuisines[cuisine] += weights[i] + 1
            else:
                badcuisines[cuisine] = weights[i]
            i+=1
for cuisine in goodcuisines:
    if cuisine in badcuisines:
        goodcuisines[cuisine] -= badcuisines[cuisine]
sortedcuisines = sorted(goodcuisines, key=goodcuisines.get, reverse = True)
print("The recommended cuisine is: " + sortedcuisines[0])
inputFile.close()
