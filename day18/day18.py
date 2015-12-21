
#import matplotlib.pyplot as plt
import numpy as np
from conway import conway

if __name__ == "__main__":
	# set up board
	m,n = 100,100

	A = np.array([ [ 1 if x=="#" else 0 for x in l.strip()] for l in open('day18.input').readlines() ]).reshape(m, n)

	#A = np.array([[0,1,0,1,0,1],[0,0,0,1,1,0],[1,0,0,0,0,1],[0,0,1,0,0,0],[1,0,1,0,0,1],[1,1,1,1,0,0]])

	print A
	for i in range(100):
		A = conway(A)
	print np.sum(A)
