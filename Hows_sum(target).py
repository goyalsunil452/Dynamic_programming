def howsum(target,num,memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for i in num:
        Reminder = target - i
        Targetresult = howsum(Reminder, num, memo)
        if Targetresult != None:
            memo[target] = [Reminder, i]
            return memo[target]
    memo[target] = None
    return memo[target]


target = int(input())
num  = list(map(int, input().split()))
print(howsum(target,num))

# m = target sum
# n = num length
# Brute force
# time = O(n^m+m)
# space = O(m)

# Memoized
# time = O(n*m^2)
# space = O(m^2)