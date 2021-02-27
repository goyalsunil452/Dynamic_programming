def howsum(target,num,memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for i in num:
        Rtarget = target - i
        tResult = howsum(Rtarget, num, memo)
        if tResult != None:
            memo[target]=[Rtarget,i]
            return memo[target]
    memo[target] = None
    return memo[target]


target = int(input())
num  = list(map(int, input().split()))
print(howsum(target,num))