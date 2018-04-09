import random
import itertools
import math
from  more_itertools import unique_everseen

	
no_of_generations=0
SA_soln=[]



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


class Simulated_Annealing:

	@staticmethod
	def E(S,variety):
		e=0
		l=len(S)
		for i in range(l):
			for j in range (i+1,l):
				x=S[i]
				y=S[j]
				dh=hamming_dist(x, y)
				if variety==0 :
					if dh==0:
						dh=1
					e+=(dh)**(-2)
				elif variety==1:
					if (dh<d):
						if dh==0:
							dh=1
						e+=((1/dh)-(1/d))**(2)
				else:
					if (dh<d):
						e+=(d-dh)**2
		return e


	@staticmethod
	def perturbation(c):
		global n 
		a=random.randint(0,len(c)-1)
		b=random.randint(0,n-1)

		if c[a][b]=="1":
			#weight remains same 
			c[a]=list(c[a])
			c[a][b]="0"
			while True:
				d=random.randint(0,n-1)
				if c[a][d]=="0" and d!=b:
					c[a][d]="1"
					break
			c[a]=''.join(c[a]) 

		elif c[a][b]=="0" and random.random()<0.1:
			#weight increases with probability 0.1
			c[a]=list(c[a])
			c[a][b]="1"
			c[a]=''.join(c[a])
		return c


	@staticmethod
	def mainSearch(seed):
		global n
		alpha=0.95
		while True:
			T=1000
			while (T>1):
				iter=0
				while (iter<20):
					iter+=1
					#two jiggles
					seed_1=Simulated_Annealing.perturbation(seed)
					delta_E=Simulated_Annealing.E(seed_1,v)-Simulated_Annealing.E(seed,v)
					if delta_E<0:
						iter+=1
						seed=seed_1
					else:
						if (random.random()> math.e**(-delta_E/T)):
							seed=seed_1
				T=alpha*T
				print(T)
			return(seed)



#---------------------------------MAIN----------------------------------#


n=int(input("Enter length of binary word \n"))
w=int(input("Enter weight \n"))
d=int(input("Enter hamming distance\n"))

for v in range (3):
	print ("variety= ",v)
	print("\n-"*10+"seed as zeroes"+"-"*10)

	seed=constant_weight_codes(n,w)
	SA_soln=Simulated_Annealing.mainSearch(seed)
	print_distribution(weight_distribution(SA_soln))

	print("="*30)
	print(len(SA_soln))
	print(list(unique_everseen(SA_soln)))
