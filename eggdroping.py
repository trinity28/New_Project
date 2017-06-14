INT_MAX = 32767
def findMinTrials(n,k):

	l= [[0 for x in range(k+1)] for x in range(n+1)]


	
	for i in range(1,n+1):
		l[i][1]=1
		l[i][0]=0
	for j in range(1,k+1):
		l[1][j]=j

	

	
	for i in range(2,n+1):
		for j in range(2,k+1):
			l[i][j]=INT_MAX
			
			for x in range(1,j+1):

				res=1+max(l[i-1][x-1],l[i][j-x])
				if res<l[i][j]:
					l[i][j]=res
		

	return l[n][k]
print "minimum nmber of trials required="
print findMinTrials(2,100)

