import random
import itertools

"""
        |   X \ {x}    x belongs to X
N(x) =  |                       removal depends on probability
        |   X\ {y} U {x}    x  belongs to H(n,w) \ x & y belongs to X

"""

################## FOR CONSTANT WEIGHT CODES ############################

iter,p=0,0
seed=[]
max_len_list=[0,0,[]]

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

            #bounding condition for random order
            if (iter>8000):
                break

            try:
                b=next(randomGenertor(binSet))
            except:
                return(seed)

            for x in seed:
                #removed if(x) statement
                if (x):
                    if (hamming_dist(x,b)<d):
                        compatibility-=1 
                        if (compatibility==0):
                            break
                        if (compatibility==1):
                        #if distance less than itis not compatibility
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


n=int(input("Enter length of binary word \n"))
w=int(input("Enter weight \n"))
binSet=constant_weight_codes(n,w)
d=int(input("Enter hamming distance\n"))

all_soln=[]

for i in range(0,10000):
    global p,iter,seed
    p=i/10000
    seed=[]
    iter=0
    heuristic_soln=HillClimbing_Better(binSet,d)
    if (len(heuristic_soln)>max_len_list[0]):
        max_len_list=[len(heuristic_soln),p,heuristic_soln]
    all_soln.append([len(heuristic_soln),p,heuristic_soln])
    print(" Length of contruct = ",len(heuristic_soln)," Probability = ",p)


print("Max len: ",max_len_list[0]," And occured at probability: ",max_len_list[1])
print("="*30)
max_len_list[2].sort()
print("Elements in max len list: ",max_len_list[2])

solution_list=[]

for l in all_soln:
    if l[0]==max_len_list[0]:
        if l[2] not in solution_list:
            solution_list.append(l[2])

solution_list.sort()

for ans in solution_list:
    for word in ans:
        print(word)
    print("\n\n")