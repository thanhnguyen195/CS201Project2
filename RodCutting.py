import random
import timeit

def rodCutRecur(l):
    max = p[l]
    for i in xrange(1,l):
        if o[i]==-1:
            o[i] = rodCutRecur(i)
        if p[l-i]==-1:
            o[l-i] = rodCutRecur(l-i)
        if max<(o[i]+o[l-i]):
            max = o[i]+o[l-i]
    return max

def rodCut1(l,n):
    global o
    o = [-1]*(n+1)
    return rodCutRecur(l)

def rodCut2(l,n):
    o = [-1]*(n+1)
    for i in xrange(1,l+1):
        o[i]=p[i]
        for j in xrange(1,i):
            if o[i]<o[j]+o[i-j]:
                o[i] = o[j]+o[i-j]
    return o[l]

def main():
    n=5000
    global p
    p = [0]
    for i in range(n):
        p.append(random.randint(0,10000))
#    return rodCut1(n,n)
#    return rodCut2(n,n)
    print timeit.timeit("rodCut1(n,n)",setup="from __main__ import rodCut1; n=5000",number=1)
    print timeit.timeit("rodCut2(n,n)",setup="from __main__ import rodCut2; n=5000",number=1)
    return

main()