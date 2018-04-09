import random
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math

x_list,y_list=[],[]

def print_distribution(lst):
	for w in lst:
		print(w[0]," "+("#"*w[1]))

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

def weight_sort(lst):
	global w
	weight_correct=[]
	for code in lst:
		if (calc_weight(code)>=w):
			weight_correct.append(code)
	return weight_correct

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


def E(S,k=2):
	e=0
	for x in S:
		for y in S:
			if x!=y and (hamming_dist(x,y)<d):
				e+=(d-hamming_dist(x,y))**2
	return e


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


def SimulatedAnnealing(seed):
	global n,x_list,y_list
	alpha=0.98

	T=1000
	while (T>1):
		iter=0
		while (iter<100):
			iter+=1
			#two jiggles
			seed_1=perturbation(perturbation(seed))
			delta_E=E(seed_1)-E(seed)
			if delta_E<0:
				iter+=1
				seed=seed_1
			else:
				if (random.random()< math.e**(-delta_E/T)):
					seed=seed_1
		T=alpha*T 
		print(T)
		x_list.append(T)
		y_list.append(E(seed))
	return(seed)
	

def result_to_heavy_weight_code(lst):
	#removeing similar elements
	global d,w

	lst=weight_sort(lst)
	r=random.randint(0,len(lst)-1)
	code=[lst[r]]
	iter=0
	while (iter<7000):
		add=1
		r=random.randint(0,len(lst)-1)
		for x in code:
			if(x):
				if (hamming_dist(lst[r],x)<d):
					add=0
		if (add==1) and (lst[r] not in code) :
			code.append(lst[r])
		iter+=1
	return(code)

def details(lst):
	global x_list,y_list
	graph_matplot.graph_main(x_list,y_list)
	print("#"*30)
	print("Weight distibution:\n")
	print_distribution(weight_distribution(lst))
	answer=result_to_heavy_weight_code(lst)
	print("Heavy weight code length construction:\nlength-",len(answer))
	print("construction- ",answer)
	x_list,y_list=[],[]


class graph_matplot:
    global n,w,d
    @staticmethod
    
    def graph_main(X,Y):
        plt.plot(X,Y)
        plt.ylabel("Energy")
        plt.xlabel("Temp")
        plt.show()

#---------------------------------MAIN----------------------------------#


n=int(input("Enter length of binary word \n"))
w=int(input("Enter weight \n"))
d=int(input("Enter hamming distance\n"))


#NO EFFECT OBSERVED ON CHANGING OF ALPHA
print("with SEED 0")
M=40
seed=[("0"*n) for i in range(0,M)]
details(SimulatedAnnealing(seed))


print("\nwith CONSTANT WEIGHT CODES")
seed=constant_weight_codes(n,w)
details(SimulatedAnnealing(seed))

