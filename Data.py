import csv
import math

with open("data.csv", newline = "") as f :
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]

#Finding mean
def mean(data) :
    sum = 0
    n = len(data)

    for i in data :
        sum = sum + int(i)

    mean = sum/n
    return mean

#Subtracting from mean & squaring
squaredList = []
for i in data :
    a = int(i) - mean(data)
    a = a**2
    squaredList.append(a)

#Summing up the squared List
sum = 0
for j in squaredList :
    sum = sum + j

#Dividing by total values (n-1)
result = sum/(len(data) -1)

#Final - square root
stdev = math.sqrt(result)

print(stdev)
print(mean(data))