import random
import itertools
import matplotlib.pyplot as plt
import numpy as np


"""
Let N(x) be the heuristic solution after hill climbing 

        |   X \ {x}    x belongs to X
N(x) =  |                       removal depends on probability
        |   X\ {y} U {x}    x  belongs to H(n,w) \ x & y belongs to X

"""

################## FOR HEAVY WEIGHT CODES ############################

iter,p=0,0
seed=[]
max_len_list=[]
max_len=[0,0]

def constant_weight_codes(n, k):          
    result = []
    for bits in itertools.combinations(range(n), k):
        s = ['0'] * n
        for bit in bits:
            s[bit] = '1'
        result.append(''.join(s))
    return (result)


def hamming_dist(x,y):         
    assert len(x) == len(y)
    count,z = 0,int(x,2)^int(y,2)
    while z:
        count += 1
        z &= z-1 
    return count

def randomGenertor(binSet):               
    while True:
        r=random.randint(0,len(binSet)-1)
        yield (binSet[r])


def HillClimbing_Better(binSet,d):

    global iter,seed
    
    while(True):
        if (len(seed)<100):
            compatibility=2
            iter+=1
            if (iter>8000):
                break

            try:
                b=next(randomGenertor(binSet))
            except:
                return(seed)

            for x in seed:
                if (x):
                    if (hamming_dist(x,b)<d):
                        compatibility-=1 
                        if (compatibility==0):
                            break
                        if (compatibility==1):
                            a=x
                        
            if (compatibility==1 and random.random()<p and len(seed)>0):
                seed.remove(a)
                if b not in seed:
                    seed.append(b)

            if compatibility==2 and b not in seed:
                seed.append(b)

        else:
            return (seed)

    return (seed)

class graph_matplot:
    global n,w,d
    @staticmethod
    
    def graph_main(X,Y):
        plt.plot(X,Y)
        plt.ylabel("Length of Solution of H("+str(n)+","+str(d)+","+str(w)+")")
        plt.xlabel("Probability")
        plt.axis([0, 1, 0, 70])
        plt.show()

#---------------------------------MAIN----------------------------------#

n=int(input("Enter length of binary word \n"))
w=int(input("Enter weight \n"))
d=int(input("Enter hamming distance\n"))

xList=[]
yList=[]

binSet=[]
for f in range(w,n+1):
    binSet=binSet+constant_weight_codes(n,f)

for i in range(0,10000):
    global p,iter,seed
    p=i/10000
    seed=[]
    iter=0

    heuristic_soln=HillClimbing_Better(binSet,d)

    if (len(heuristic_soln)>max_len[0]):
        max_len=[len(heuristic_soln),p]
        max_len_list=heuristic_soln

    xList.append(p)
    yList.append(len(heuristic_soln))

    print(p)

graph_matplot.graph_main(xList,yList)

print("="*30)
print("Max len: ",max_len[0]," And occured at probability: ",max_len[1])
print("H(",n,",",d,",",w,")")
print("Elements in max len list: ",max_len_list)
