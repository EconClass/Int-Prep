# ==============================PROBLEM==============================
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Restatement:
# Given an array nums find the length of an array where all occurances of a value val are removed from nums.
# All memory created must be O(1) space complexity, but you are allowed to modify the input array.


# ==============================CLARIFICATION==============================
# Are all elements in the array the same type?
# Are the elements ordered?
# Can I use built-in python functions?


# ==============================ASSUMTIONS==============================
# Output is an int
# Array is unsorted
# There are negatives


# ==============================SOLUTIONS==============================
# Complexity:
#     - S = space complexity
#     - R = worst case runtime complexity

# First attempt
def removeElement(nums=[], val=None): # S: O(1) R: O(2n) -> O(n)
    occ = 0 # S: O(1)
    for num in nums: # R: O(n)
        if num == val: # R: O(1)
            occ += 1 # R: O(1)
    
    for _ in range(occ): # R: O(n)
        nums.remove(val) # R: O(n)

    return len(nums)# R: O(1)

# Optimized for runtime complexity
def remove_element(nums=[], val=None): # S: O(1) R: O(n)
    occ = 0 # S: O(1)

    for num in nums: # R: O(n)
        if num != val: # R: O(1)
            occ += 1  # R: O(1)
    
    return occ

if __name__ == "__main__":
    test_list = [0,1,2,2,3,0,4,2]
    target = 2
    assert removeElement(test_list, target) == 5
    print(removeElement(test_list, target))
