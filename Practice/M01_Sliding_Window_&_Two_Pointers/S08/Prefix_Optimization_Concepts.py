from typing import List
def runningSum( nums: List[int]) -> List[int]:
        res=[0]*(len(nums))
        for i in range(len(nums)):
            curr_sum=0
            for j in range(0,i+1):
                curr_sum+=nums[j]
            res[i]=curr_sum
        return res
nums=[1,2,3,4]
print(runningSum(nums))