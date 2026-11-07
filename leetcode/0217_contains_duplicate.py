
def has_duplicate(nums):
    for i in range(len(nums)) :
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

print(has_duplicate([2,3,4,5,6,7]))
print(has_duplicate([2,3,4,3,6,7]))

def has_duplicate2(nums):
    seen = {}
    for num in nums:
        if num not in seen:
            seen[num] = 1
        else:
            return True
    return False
print(has_duplicate2([2,3,4,5,6,7,2]))
print(has_duplicate2([1,2,3,4,5,6,7]))
