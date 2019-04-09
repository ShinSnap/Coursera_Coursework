def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in nums: 
            match = target - num
            print(nums.index(num),nums.index(match))
            if match in nums and nums.index(num) != nums.index(match):
                print(nums.index(num),nums.index(match))
                

nums = [3,3]
target = 6
final = []
twoSum(final,nums,target)   