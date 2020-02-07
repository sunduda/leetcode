from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    ans = []
    # Attempt 2:
    #   One-pass hash table method
    hashmap = dict()
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap.keys():
            ans = [hashmap[complement], i]
            break
        else:
            hashmap[nums[i]] = i
    # Attempt 1:
    #   Brute force
    # for i in range(len(nums) - 1):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             ans = [i, j]
    #             break
    return ans
