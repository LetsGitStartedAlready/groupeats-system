import operator
inputFile = open("CuisineTestData.txt")
lines = inputFile.readlines()
goodcuisines = {}
badcuisines = {}
for x in range(len(lines)):
    if (x%3==1): 
        line = lines[x].split()
        weight = 3
        for cuisine in line:
            if cuisine in goodcuisines:
                goodcuisines[cuisine] += weight + 1
            else:
                goodcuisines[cuisine] = weight
            weight-=1
    if (x%3==2):
        line = lines[x].split()
        weight = 3
        for cuisine in line:
            if cuisine in badcuisines:
                badcuisines[cuisine] += weight + 1
            else:
                badcuisines[cuisine] = weight
            weight-=1
for cuisine in goodcuisines:
    if cuisine in badcuisines:
        goodcuisines[cuisine] -= badcuisines[cuisine]
sortedcuisines = sorted(goodcuisines, key=goodcuisines.get, reverse = True)
print("The recommended cuisine is: " + sortedcuisines[0])
inputFile.close()
