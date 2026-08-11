'''from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
    max_sum = float("-inf")
    n=len(nums)
    for i in range(n-k+1):
        sub_sum=0
        for j in range(i,i+k):
            sub_sum += nums[j]
        max_sum = max(max_sum, sub_sum)
    return max_sum / k
nums=[1,12,-5,-6,50,3]
print(findMaxAverage(nums,4))'''

'''from typing import List
def findMaxAverage_Optimal(nums: List[int], k: int) -> float:
    max_sum = sum(nums[:k])
    current_sum = max_sum
    n=len(nums)
    for i in range(0,n-k):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum / k
nums=[1,12,-5,-6,50,3]
print(findMaxAverage_Optimal(nums,4))'''

from typing import List
def numOfSubarrays(nums: List[int], k: int, threshold: int) -> int:
    count = 0
    n=len(nums)
    for i in range(n-k+1):
        sub_sum=0
        for j in range(i,i+k):
            sub_sum += nums[j]
        if sub_sum/k >= threshold:
            count += 1
    return count
nums=[2,2,2,2,5,5,5,8]
print(numOfSubarrays(nums,3,4))