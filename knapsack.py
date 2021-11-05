#https://exercism.org/tracks/python/exercises/knapsack
#https://www.pythonpool.com/knapsack-problem-python/
#https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
def printformat(nlist, row):
    if row == 0:
        teller = 0
        for n in nlist:
            if teller > 0:
                print('{:2d}'.format(teller), end=' ')
            else:
                print('   ', end = '')
            teller += 1
        print()
    else:
        if row > 0:
            nlist[0] = gewichten[row-1]
    for n in nlist:
        print('{:2d}'.format(n), end = ' ')
    print()
    if (row > 0):
        nlist[0] = 0

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                              + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
        printformat(K[i],i)
    return K[n][W]

#Sample
gewichten = [5,4,6,4]
waarden = [10,40,30,50]
Rugzakgewicht = 10
n = 4
print('maximum value: ' + str(knapSack(Rugzakgewicht,gewichten,waarden,4)))

#Another one
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
#print(knapSack(W, wt, val, n))
