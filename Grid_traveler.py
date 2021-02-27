# using P&C
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

def gridtraveler(m,n):
    r=n-1
    d=m-1
    return factorial(r+d)//(factorial(r)*factorial(d))

m, n = map(int, input().split())
print(gridtraveler(m, n))

'''
# using Dynamic programming
memo = {(0,0):0,(1,0):0,(0,1):0,(1,1):1}
def gridtraveler(m,n,memo):
    global val
    val = 0
    key = (m, n)
    if key in memo:
        val = memo[(m, n)]
        return val

    if m == 0 or n == 0:
        val = 0
        return val

    else:
        val = gridtraveler(m-1, n, memo) + gridtraveler(m, n-1, memo)
    memo[key] = val

    return val



m, n = map(int, input().split())
print(gridtraveler(m, n,memo))
'''
'''
#using recursion
def Gridtraveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return Gridtraveler(m-1,n) + Gridtraveler(m,n-1)


m,n = map(int,input().split())
print(Gridtraveler(m,n))
'''


