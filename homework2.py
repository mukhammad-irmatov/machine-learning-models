import numpy as np
import math
points= np.array([[1, 1],
                 [2, 1],
                 [4, 3 ],
                 [5, 4]])
centroids = {'c1':[1,1],'c2':[2,1]}

def Dist(points,centroids,val):
    distances = []
    for x in range(len(points)):
        dist = round(math.sqrt((points[x][0]-centroids[val][0])**2+((points[x][1]-centroids[val][1])**2)),2)
        distances.append(dist)
    return distances
# #find distance to centroid 1 (c1)
def assign_classes():
    distance1 = Dist(points,centroids,"c1")
    # #find distance to centroid 2 (c2)
    distance2 = Dist(points,centroids,"c2")
    #assign to classes
    class1 = []
    class2 = []

    for x in range(len(distance1)):
        if distance1[x]<distance2[x]:
            class1.append(points[x])
        else:
            class2.append(points[x])

    return class1, class2
print(assign_classes())
class1 = assign_classes()[0]
class2 = assign_classes()[1]
print(class1[0][0])

def find_centroid():
    c1 = sum(class1[0][0])/len(class1[0][0])
    return c1
print(find_centroid())