import random
import itertools
import math
	
no_of_generations=0
SA_soln=[]

def weight_distribution(lst):
	global n 
	weight_dist=[[i,0] for i in range(n+1)]
	for x in lst:
		w=x.count('1')
		weight_dist[w][1]+=1
	return weight_dist


def calc_weight(string):
	return string.count('1')


def constant_weight_codes(n,k):          
    # returns list of all binary strings of length n and weight k
    result = []
    for bits in itertools.combinations(range(n), k):
        s = ['0'] * n
        for bit in bits:
            s[bit] = '1'
        result.append(''.join(s))
    return (result)


def hamming_dist(x,y):       
    # returns hamming distance between two strings
    #hamming distance calculated by using 'AND' operartion rather than conventional 'ROR' which results in 50% faster running time           
    # "^"- XOR operator   
    assert len(x) == len(y)
    count,z = 0,int(x,2)^int(y,2)
    while z:
        count += 1
        z &= z-1 
    return count


class Simulated_Annealing:

	@staticmethod
	def E(S,k=2):
		e=0
		for x in S:
			for y in S:
				if x!=y:
					e+=(hamming_dist(x,y))**(-k)
		return e


	@staticmethod
	def perturbation(c):
		global n 
		a=random.randint(0,len(c)-1)
		b=random.randint(0,n-1)
		if c[a][b]=="1":
			c[a]=list(c[a])
			c[a][b]="0"
			c[a]=''.join(c[a])
		else:
			c[a]=list(c[a])
			c[a][b]="1"
			c[a]=''.join(c[a])
		return c


	@staticmethod
	def mainSearch(seed):
		global n
		alpha=0.9
		while True:
			T=1000
			while (T>1.5):
				iter=0
				while (iter<20):
					iter+=1
					#two jiggles
					seed_0=Simulated_Annealing.perturbation(seed)
					seed_1=Simulated_Annealing.perturbation(seed_0)
					delta_E=Simulated_Annealing.E(seed_1)-Simulated_Annealing.E(seed)
					if delta_E<0:
						iter+=1
						seed=seed_1
					else:
						if (random.random()> math.e**(-delta_E/T)):
							seed=seed_1
				T=alpha*T
			return(seed)


	@staticmethod
	def seed_50_generator(lst):
		while True:
			seed_50=[]
			for counter in range(0,50):
				r=random.randint(0,len(lst)-1)
				seed_50.append(lst[r])
			yield (seed_50)


	@staticmethod
	def weight_sort(lst):
		global w
		weight_correct=[]
		for code in lst:
			if (calc_weight(code)>=w):
				weight_correct.append(code)
		return weight_correct


	@staticmethod
	def optimized_seed_addition(lst,nonzero=0):

		global SA_soln,no_of_generations,n,d

		for j in range (40):
			for i in range (70):
				if nonzero==1:
					seed_small=next(Simulated_Annealing.seed_50_generator(lst))
				else :
					seed_small=["0"*n]*50
				lst=Simulated_Annealing.weight_sort(Simulated_Annealing.mainSearch(seed_small))
				SA_soln.append(lst)
			
			SA_soln=HillClimb.HillClimbing_Short(SA_soln)
			print("length =",len(SA_soln), "\nSoln is :",SA_soln)
			print("#"*30)


###################  HILL CLIMBING #############################

class HillClimb:

	@staticmethod
	def randomGenertor(binSet):               
	    # genrates a random string from the argument list binSet
	    while True:
	        r=random.randint(0,len(binSet)-1)
	        yield (binSet[r])


	@staticmethod
	def HillClimbing_Short(binSet):

	    # efficient to use global variable iter and seed rather than recursively calling the function HillClimbing_Better
	    global SA_soln,n,d
	    iter=0
	    p=0.75
	    while(True):
	        #len(seed)<100 condition caps the result if the function runs into an error , should be changed while computing larger H(n,d,w)
	        if (len(SA_soln)<1000):
	            compatibility=2
	            iter+=1
	            #bounding condition for random order 
	            if (iter>1000):
	                break

	            try:
	                # b is random element selected from binSet
	                b=next(HillClimb.randomGenertor(binSet))
	            except:
	                return(SA_soln)

	            for x in SA_soln:
	                # if there is an element in the list then proceed 
	                if (x):
	                    if (hamming_dist(x,b)<d):
	                        compatibility-=1 
	                        if (compatibility==0):
	                            break
	                        if (compatibility==1):
	                            #compatibility is 1 iff one member in seed exist that has hamming distance than string generated,replacement of that string depends on probability
	                            a=x
	                        
	            if (compatibility==1 and random.random()<p and len(SA_soln)>0):
	                SA_soln.remove(a)
	                #seed removal with probability p which is a changing parameter in our study
	                if b not in SA_soln:
	                    SA_soln.append(b)

	            if compatibility==2 and b not in SA_soln:
	                SA_soln.append(b)

	        else:
	            return (SA_soln)

	    return (SA_soln)


#---------------------------------MAIN----------------------------------#


n=int(input("Enter length of binary word \n"))
w=int(input("Enter weight \n"))
d=int(input("Enter hamming distance\n"))

print("-"*10+"seed as zeroes")

Simulated_Annealing.optimized_seed_addition([])

print("#"*30)
print(len(SA_soln))
print(SA_soln)


print("-"*10+"seed as haevy weight")
seed=[]
for weight in range(w,n+1):
	seed+=constant_weight_codes(n,w)
SA_soln=[]
no_of_generations=0
Simulated_Annealing.optimized_seed_addition(seed,1)
