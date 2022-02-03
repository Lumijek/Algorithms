from random import shuffle
import time
from array import array

x = list(range(10000000))
shuffle(x)
print(len(x))

#VERSION 1
def mergesort(n):

	if len(n) <= 1:
		return n

	length = len(n) // 2
	A = mergesort(n[:length])
	B = mergesort(n[length:])
	iterA = 0
	iterB = 0
	C = []
	for i in range(len(n)):
		if A[iterA] < B[iterB]:
			C.append(A[iterA])
			iterA += 1
		elif B[iterB] < A[iterA]:
			C.append(B[iterB])
			iterB += 1
		if iterA == len(A):
			C += B[iterB:]
			break
		if iterB == len(B):
			C += A[iterA:]
			break
	return C

#VERSION 2
def merge_sort(n):

	if len(n) <= 1:
		return n

	length = len(n) // 2
	A = mergesort(n[:length])
	B = mergesort(n[length:])
	iterA = 0
	iterB = 0
	iterC = 0
	C = array('i', [0] * len(n))
	for i in range(len(n)):
		if A[iterA] < B[iterB]:
			C[iterC] = A[iterA]
			iterA += 1
			iterC += 1
		elif B[iterB] < A[iterA]:
			C[iterC] = B[iterB]
			iterB += 1
			iterC += 1
		if iterA == len(A):
			for t in range(len(B[iterB:])):
				C[iterC] = B[iterB]
				iterB += 1
				iterC += 1
			break
		if iterB == len(B):
			for t in range(len(A[iterA:])):
				C[iterC] = A[iterA]
				iterB += 1
				iterC += 1
			break
	return C
