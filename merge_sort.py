from array import array

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

