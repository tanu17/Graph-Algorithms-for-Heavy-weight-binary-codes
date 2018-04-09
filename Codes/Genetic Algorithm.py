import random 
import copy,math

"""
code size 	S  (M)
length 	L  (n)
weight	w
D min 	d

"""
avg_sum=0
avg_count=0
max

def hamming_dist(x,y):
    assert len(x) == len(y)
    count,z = 0,int(x,2)^int(y,2)
    while z:
        count += 1
        z &= z-1 
    return count

def cost(code):
	global n,d,avg_sum,avg_count
	f_list=[]
	f=0
	sum_d=0
	l=len(code)
	for i in range(l):
		for j in range (i+1,l):
			x=code[i]
			y=code[j]
			if (hamming_dist(x,y)<d):
				sum_d+=1/((hamming_dist(x,y)**2)+1)
			else:
				sum_d+=1/((d**2)+1)
	avg_sum+=f
	avg_count+=1
	f=f-sum_d
	f_list.append([f,code])
	return f_list

def exponential_scaling(f):
	avg = sum([a[0] for a in f])/len(f)
	max_f = (max(f))[0]
	f.sort()
	for x in f:
		x[0]=math.e**(2*(x[0]-avg)/(max_f-avg))

def rank_selection(f):
	global M
	f.sort()
	l=len(f)
	reproduction_pool=[]
	for i in range(0,l,l//M):
		reproduction_pool.append(f(i))
	return(reproduction_pool)

def crossover(pool):
	global prob_crossover
	l=len(pool)
	new_pool=[]
	while len(new_pool)<prob_crossover*l:
		p=k=random.randint(0,len(pool)-1)
		a,b=pool.pop(p),pool.pop(k)
		









