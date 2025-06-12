import math

def minEatingSpeed(self, piles, h): #Return the minimum integer "k" such that you eat all the bananas within h
    # piles = [1,4,3,2], h = 9 
    #                          l m   r
    # k = [1...max(piles)] -> [1,2,3,4]
    l,r = 1, max(piles)
    res = r

    while l <= r:
        m = l + (r - l) // 2 #k
        suma = 0

        for i in piles:
            # determine the sum of hours that koko is going to take based on m(k)
            suma += math.ceil(i / m)
        # if the result is less than 'h'
        if suma <= h:
            res = min(res, m)
            r = m - 1
        else: # if the result is greater than 'h'
            l = m + 1
    return res




