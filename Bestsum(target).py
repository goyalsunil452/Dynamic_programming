# Shorted length of sum return
def Bestsum(target,num,memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    shortestCombination = None
    for i in num:
        Reminder = target - i
        remindercom = Bestsum(Reminder, num, memo)
        if remindercom != None:
            Combinationlist = remindercom[:]
            Combinationlist.append(i)
            if (shortestCombination==None or len(Combinationlist)<len(shortestCombination)):
                shortestCombination =Combinationlist

    memo[target] =shortestCombination
    return shortestCombination

"""
def Bestsum(target,num):
    if target == 0:
        return []
    if target < 0:
        return None
    shortestCombination = None
    for i in num:
        Reminder = target - i
        remindercom = Bestsum(Reminder, num, memo)
        if remindercom != None:
            Combinationlist = remindercom[:]
            Combinationlist.append(i)
            if (shortestCombination==None or len(Combinationlist)<len(shortestCombination)):
                shortestCombination =Combinationlist

    return shortestCombination
"""

target = int(input())
num  = list(map(int, input().split()))
print(Bestsum(target,num))

# m = target sum
# n = num length
# Brute force
# time = O(n^m+m) exponential
# space = O(m^2)

# Memoized
# time = O(m^2*n)
# space = O(m^2)
