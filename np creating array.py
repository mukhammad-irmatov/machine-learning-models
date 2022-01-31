import numpy as np
#massiv hosil qilamiz
massiv1 = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]])
for x in massiv1:
    for y in x:
        if(y%5==0):
            print(y)
