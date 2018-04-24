# Heuristic Construction(Informed Search) of Heavy Weight Binary Codes

A constant weight binary code is a set of binary vectors of length n, with weight at least w and minimum Hamming distance d. We refer to the maximum possible number of codewords  in a heavy weight code as H(n, d, w). 

Heavy weight codes have applications in asynchronous communication problems and codes from simultaneous transfer of energy and information.

In this project, we study and experiment with many local search heuristic and determine their effectiveness as the novel methods for finding heavy weight codes with the maximum number of codewords. 

The algorithms studied were- 
	Greedy Algorithm
	Hill Climbing Algorithm
	Simulated Annealing
	Tabu Search
Alongside the study for optimizing the search of Heavy Weight binary codes, we got glimpse upon related problems such as Genetic Algorithm, t-Covering Design Problem and for finding constant weight binary codes which helped us in understanding the original problem in depth.


# Greedy Algorithm:

Description-
Greedy algorithm works on the principle of brute force by checking each solution. In this case, if the codeword selected for checking is found to be feasible, it is added to the code. There are two types of greedy search algorithm used- random search and lexicographic search. In lexicographic search, the exploration order is in the alphabetic/numerical order which can in turn be ascending or descending. In random search, there is no exploration order and the probability of codeword being selected is equal for all codewords.
 

Pseudo Code-
	
	Lexicographic:

	Let length of codeword be n, weight be w, hamming distance d 
	H (n,w)={ x ε F2 : weight(x)>=w and |x|=n}
	C = Φ 
	While |C |<M or some terminating condition:
		1.Pick x ε H (n,w) in order
		2.If hamming distance between x and y >=d for all y ε C
			Add x to C

	Random:

	Let length of codeword be n, weight be w, hamming distance d 
	H (n,w)={ x ε F2 : weight(x)>=w and |x|=n}
	C = Φ 
	While |C |<M or some terminating condition:
		1.Randomly pick x ε H (n,w) in order
		2.If hamming distance between x and y >=d for all y ε C
			Add x to C


Result-
For lexicographic order, the results obtained were not satisfactory as expected, as the code gets stuck in the local optima and the length of the code is always same for any number of trials.
For random search, the results obtained were better than lexicographic order but still far from the ideal result required. The random search tends to get stuck in local optima and the result obtained from one trial can vary from the other trial with the same initial conditions of n,d,w.
Example: After several trial the best lower bound obtained from greedy search was 22 for H(10,4,5) which was proved later on in the research to be 37.


# Hill Climbing Algorithm:

Description-
Greedy algorithm works on the principle of brute force by checking each solution. In this case, if the codeword selected for checking is found to be feasible, it is added to the code. There are two types of greedy search algorithm used- random search and lexicographic search. In lexicographic search, the exploration order is in the alphabetic/numerical order which can in turn be ascending or descending. In random search, there is no exploration order and the probability of codeword being selected is equal for all codewords.
 

Pseudo Code-

	Let length of codeword be n, weight be w, hamming distance d 
	H (n,w)={ x ε F2 : weight(x)>=w and |x|=n}
	X= Φ 
	While |C |<M or some terminating condition:      	  

	   Neighbourhood of X is defined as:

	      |      X υ {x}     where x doesn’t belong to X 
	 N(X)=|	     X\{y}  υ {x}      remove y with some probability or   
	      |                       when certain conditions are satisfied
	      |                       where y ε X , x ε H (n,w) and     
	      |                                         x doesn’t belong to X
		x is randomly generated from H (n,w)
		X <- N    (X)

Result-
The algorithm had been successful in finding optimal heavy weight codes. Due to removal of existing codeword from the code (with some probability), the code is prevented from getting bound in local optima and ultimately achieving global optima.
Example: The algorithm was able to find many codes with code size equal to upper bound- H(10,4,5), H(10,4,5), H(10,9,5), H(11,3,5) etc.


Simulated Annealing Algorithm:

Description-
Simulated annealing derives a virtual analogy between the process of annealing which is cooling and heating of metal to make it stronger. Similarly, this algorithm uses temperature as a control parameter. Trapping into local optima is avoided by selection of a bad codeword with a probability of e-ΔE/T , which depends on the control parameter T.

Pseudo Code-

	Let length of codeword be n, weight be w, hamming distance d. 
	Energy= ∑_(x,yε C and x≠y)▒〖d(x,y)〗^(-2) 
	Choose code C,  , temperature T
	(Here initial temperature=1000 and temperature lowered in GP with ratio 0.9 and no of energy drops 3-5 for lowering temp.)
	While |C |<M or some terminating condition:      	  			 
		Until several energy drops or too many iterations
	1.C   ’ <- perturbation(C  )
	2. Let ΔE = energy(C   ’) – energy(C  )
	If ΔE<0
		Then C   <- C   ’
	Else
		With probability e-ΔE/T
			C   <- C   ’
	3. Lower Temperature
		

Result-
The implementation of algorithm proved to be unsuccessful. Even using better energy function resulted in negative results.


# Tabu Search:

Description-
Tabu Search avoids the trap of local optima by using memory. A list is maintained throughout the execution which contains the taboo codes and are not added to the final solution. The algorithm is an iterative one, it starts with code size 1 for particular n,d,w and keeps on increasing the code size until the optimal code is found out. 

Pseudo Code-

	Let length of codeword be n, weight be w, minimum hamming distance d, code size M. 
	Energy= ∑_(x,yε C,x≠y and d(x,y)<d)▒〖[d-d(x,y)]〗^2   
	Until (higher M can’t produce energy=0) 
	Tabu list=[]
	Choose initial code Ca
	While energy =/=0 or some terminating condition:  
		Neighbourhood of X is defined as:             

	Where cai refers to ith codeword of Ca

	2. Cb <- minimum energy code in N    (Ca) but not belonging to tabu list
	3. tabu list append(Cb )
		

Result-
The implementation of algorithm proved to be successful for constant weight codes and was found to be more efficient than previous algorithms. The constant weight code obtained matched the best codes in literature.
But implementation for heavy weight code proved to be unsuccessful as all experiments on cost function ultimately favoured choosing of constant weight codes and hence resulted in very less number of codewords in the code.





The lower bounds obtained throughout the research are available on –

https://drive.google.com/drive/folders/0Bw2pvIn5EcFDQllKUk43cGZQVFE?usp=sharing

Several of the lower bounds obtained match the actual upper bounds for the respective codes and hence resulted in calculating the exact value of the heavy weight code. 
