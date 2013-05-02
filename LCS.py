import random
import string
import timeit

def lcsrecur(i,j):
    if i==0 or j==0:
        return o[i][j]
    else:
        if str1[i]==str2[j]:
            if o[i-1][j-1]==-1:
                o[i-1][j-1]=lcsrecur(i-1,j-1)
            o[i][j]=o[i-1][j-1]+1
        else:
            if o[i-1][j]==-1:
                o[i-1][j]=lcsrecur(i-1,j)
            if o[i][j-1]==-1:
                o[i][j-1]=lcsrecur(i,j-1)
            o[i][j]=max(o[i][j-1],o[i-1][j])
        return o[i][j]

def lcs1(n,m):
    global o
    o = [[-1 for i in range(m)] for j in range(n)]
    for i in range(n):
        if str1[i]==str2[0]:
            o[i][0]=1
        else:
            if i==0:
                o[i][0]=0
            else:
                o[i][0]=o[i-1][0]
    for i in range(m):
        if str2[i]==str1[0]:
            o[0][i]=1
        else:
            if i==0:
                o[0][i]=0
            else:
                o[0][i]=o[0][i-1]
    return lcsrecur(n-1,m-1)

def lcs2(n,m):
    o = [[-1 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0 or j==0:
                if str1[i]==str2[j]:
                    o[i][j]=1
                else:
                    if i==0 and not j==0:
                        o[i][j]=o[i][j-1]
                    elif j==0 and not i==0:
                        o[i][j]=o[i-1][j]
                    else:
                        o[i][j]=0
            else:
                if str1[i]==str2[j]:
                    o[i][j]=o[i-1][j-1]+1
                else:
                    o[i][j]=max(o[i-1][j],o[i][j-1])
    return o[n-1][m-1]

def main():
    global str1,str2
    n=5000
    str1=''.join([random.choice(string.ascii_letters) for i in range(n)])
    str2=''.join([random.choice(string.ascii_letters) for i in range(n)])
    #print timeit.timeit("lcs1(n,n)",setup="from __main__ import lcs1; n=500",number=1)
    print timeit.timeit("lcs2(n,n)",setup="from __main__ import lcs2; n=5000",number=1)

main()