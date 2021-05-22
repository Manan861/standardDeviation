import math
import csv

with open('data.csv', newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]
#calculating means(step 1)
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    
    mean=total/n
    return mean

#step 2 and step 3

square_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    square_list.append(a)

#sum of all the numbers(step 4)

sum=0
for i in square_list:
    sum=sum+i


#divide the sume of the squares by n-1(step 5)

result=sum/(len(data)-1)

#take square root of the result(step 6)

sd=math.sqrt(result)
print(sd)



