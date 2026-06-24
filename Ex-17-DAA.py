def tower(p,row,g):
    dp=[[0]*100 for _ in range(100)]
    dp[0][0]=p

    for i in range(row):
        for j in range(i+1):
            x=max(0,(dp[i][j]-1)/2)
            dp[i+1][j]+=x
            dp[i+1][j+1]+=x

    return min(1,dp[row][g])

print(tower(2,1,1))
