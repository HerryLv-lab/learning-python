"""
def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
    return[]
print(two_sum([2,7,11,15],26))
"""

def two_sum(nums,target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return[seen[complement],i]
        else:
            seen[nums[i]] = i
    return[]
if __name__ == "__main__":
    print(two_sum([2,7,11,15],26))


