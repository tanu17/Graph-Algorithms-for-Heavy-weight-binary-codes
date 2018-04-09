import random 
import copy
import itertools
import matplotlib.pyplot as plt


iters=0
iter_max=1000
L=50
tabu_list=[[]]   # to see  []
prev_best=[0,[]]
add_count=0
xList,yList=[],[]

def constant_weight_codes(n, k):          
    result = []
    for bits in itertools.combinations(range(n), k):
        s = ['0'] * n
        for bit in bits:
            s[bit] = '1'
        result.append(''.join(s))
    return (result)

def randomGenertor(binSet):
    while True:
        r=random.randint(0,len(binSet)-1)
        yield (binSet[r])

def hamming_dist(x,y):
    assert len(x) == len(y)
    count,z = 0,int(x,2)^int(y,2)
    while z:
        count += 1
        z &= z-1 
    return count

def cyclic_generator(a):
	b=list(a)
	while True:
		b=[b.pop()]+b
		b_str=''.join(b)
		yield (b_str)

def perturbation(c):
	global n,w

	c_new_list=[]
	c=list(c)
	zero_list=[]
	one_list=[]
	for index in range(n):
		if c[index]=="0":
			zero_list.append(index)
		else:
			one_list.append(index)
	for zero_index in zero_list:
		for one_index in one_list:
			c_new=copy.copy(c)
			c_new[zero_index]="1"
			#probability of 0.8 that number of one increases
			p=random.random()
			if p<0.3:
				c_new[one_index]="0"
			c_new=''.join(c_new)
			if c_new.count("1")>=w:
				c_new_list.append(c_new)
	if zero_list==[]:
		for one_index in one_list:
			c_new=copy.copy(c)
			p=random.random()
			if p<0.7:
				c_new[one_index]="0"
			c_new=''.join(c_new)
			if c_new.count("1")>=w:
				c_new_list.append(c_new)
	return c_new_list

def C_0_generator():
	global n,w,M

	a="1"*w+"0"*(n-w)
	C_0=[a]
	b=cyclic_generator(a)
	for i in range (M-1):
		C_0.append(next(b))
	return(C_0)

def Neighbourhood_gen(Code,i):
	global n,w

	neighbourhood=[]
	codeword=Code[i]
	new_cword_list=perturbation(codeword)
	for j in new_cword_list:
		Code_new=copy.copy(Code)
		Code_new[i]=j
		neighbourhood.append(Code_new)
	return (neighbourhood)


def E(S):
	global d
	e=0
	l=len(S)
	for i in range(l):
		for j in range (i+1,l):
			x=S[i]
			y=S[j]
			x_w=x.count("1")
			y_w=y.count("1")

			if (hamming_dist(x,y)<d):
				e+=((d-hamming_dist(x,y))**2)/max(x_w,y_w)
	return e

def C_b_calculator(neighbourhood):
	global tabu_list
	if len(neighbourhood)==0:
		print("DVADVADVAVQEV")
	C_b=neighbourhood[0]
	minE=E(C_b)
	for q in neighbourhood:
		if q not in tabu_list:
			e=E(q)
			if e<minE:
				C_b=q
				minE=e
	return (C_b,minE)

def add(lst,element):
	global add_count,L

	if add_count>=L:
		lst.pop()
		lst=[element]+lst
	else:
		add_count+=1
		lst.append(element)
	return lst

def tabu_search(C_0):
	global M,iters,prev_best,tabu_list,iter_max,xList,yList

	print("M= ",M)

	C_a=C_0
	e=E(C_0)
	
	
	while (iters<iter_max and e!=0):
		i=iters%M
		N=Neighbourhood_gen(C_a,i)
		C_a,e=C_b_calculator(N)
		"""
		if M==21:
			xList.append(iters)
			yList.append(e)
		"""
		tabu_list=add(tabu_list,C_a)
		iters+=1
		if e==0:
			print(C_a)
			break

	if (e!=0):
		return 0
	prev_best=[M,C_a]
	
	return 1
	

class graph_matplot:
    global n,w,d
    @staticmethod
    
    def graph_main(X,Y):
        plt.plot(X,Y)
        plt.ylabel("Cost")
        plt.xlabel("Move Number")
        plt.show()


n=10
w=5
d=4
M=1
C_0=C_0_generator()
T=tabu_search(C_0)
while T!=0 :
	tabu_list=[[]]
	iters=0
	C_0=C_0_generator()
	T=tabu_search(C_0)
	M+=1

print("="*30)
print(prev_best)
