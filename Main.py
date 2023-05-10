from Iris import Iris
from Groups import Groups
from Centroid import Centroid

rawdata = []
inputFile = input("Podaj nazwę pliku, z którego skrypt ma pobrać dane")


with open(inputFile) as f:
    while True:
        line = f.readline().strip()
        rawdata.append(line)
        if not line:
            break
rawdata.pop()
data = []

for i in rawdata:
    line1 = i.split(",")
    speciment = line1[len(line1) - 1]
    iris = Iris(i, speciment)
    data.append(iris)

k = int(input("Podaj liczbę K"))

centroids = [k]

for i in range(k):
    centroids.append(data[i].inputarray)
centroids.remove(k)
groups = []
for a in centroids:
    groups.append(Groups(a))
oldgroups=[0]*k


on=True
while on:
    for l in data:
        initDistance = 0
        for dd in range(len(centroids)):
            for vector1 in range(len(data[0].inputarray)):
                initDistance = initDistance + pow(float(centroids[dd][vector1]) - float(l.inputarray[vector1]), 2)
        min = initDistance
        centr = 0
        for j in centroids:
            distancePow = 0
            for vector in range(len(centroids[0])):
                distancePow = distancePow + pow(float(j[vector]) - float(l.inputarray[vector]), 2)
            if distancePow < min:
                min = distancePow
                centr = centroids.index(j)

        groups[centr].listOfElements.append(l)
    newCentroids=[]
    for g in groups:

        newCentroid = Centroid(len(centroids[0]))

        for g1 in g.listOfElements:
            for g2 in range(len(g1.inputarray)):
                newCentroid.inputarray[g2]+=float(g1.inputarray[g2])
        for g3 in range(len(centroids[0])):
            newCentroid.inputarray[g3]=newCentroid.inputarray[g3]/len(g.listOfElements)
        newCentroids.append(newCentroid.inputarray)

    for y in range(len(groups)):
        if groups[y].listOfElements==oldgroups[y]:
            on=False
    for ttt in range(k):
        oldgroups[ttt] = groups[ttt].listOfElements

    centroids=newCentroids

    for group in range(len(groups)):
        groups[group].centroid=centroids[group]
    for b in range(len(groups)):
        for oo in groups[b].listOfElements:

            print("Do grupy "+str(b)+" należy: "+str(oo.speciment))
            sum=0
        for ooo in groups[b].listOfElements:
            for rrr in range(len(centroids[0])):
                sum=sum+pow(float(oo.inputarray[rrr])-float(ooo.inputarray[rrr]),2)
        print("Suma kwadratów odległości dla grupy " + str(b) + " wynosi: "+str(sum))
    #for asdasd in range(len(groups)):
        #print("Grupa "+str(asdasd)+" : "+str(centroids[asdasd]))




