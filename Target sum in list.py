# if you can add no in list in such a way that you can get target sum (300 [4 2] ) => True
def cansum(target,num,memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for i in num:
        Rtarget = target - i
        if cansum(Rtarget, num, memo):
            memo[target] = True
            return memo[target]
    memo[target] = False
    return memo[target]
"""
# if you add no in list in order get target each element must add once
def cansum(target,num):
    l = {}
    for i in num:

        if target-i==0:
            l[i]=(i,target-i)
        elif target - i in num:
           l[i]=(i,target-i)

    if l:
        return True
    else:
        return False
"""


"""
def cansum(target,num):
    if target == 0:
        return True
    if target < 0:
        return False
    for i in num:
        Rtarget = target - i
        if cansum(Rtarget, num):
            return True
    return False

"""
target = int(input())
num  = list(map(int, input().split()))
print(cansum(target,num))