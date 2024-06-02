class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, val in enumerate(nums):
            diff = target - val

            if val in dic.keys():
                return [dic[val], index]
            dic[diff] = index
            