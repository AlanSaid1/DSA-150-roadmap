def findMinBruteForce(self,nums): #T: O(n), S: O(1)
    return min(nums)

# -----------------------------

def findMin(self, nums): #T: O(log n), S: O(1)
    l, r = 0, len(nums) - 1

    while l < r:
        m = l + (r - l) // 2 #Esta es una forma de evitar overflow, y hasta aqui se hace todo igual que en un binary search convencional
        if nums[m] > nums[r]: #if this is true, this means that 'm' is in the bigger sorted part of the array, so the minimum number must be at the right part, thats why we move our pointers to keep looking but just in the right part.
            l = m + 1
        else: # This means that we're currently in the smaller part of the sorted array so we inmediatly discard the right part of the array by moving the right pointer with 'm'.
            r = m
    return nums[l]
