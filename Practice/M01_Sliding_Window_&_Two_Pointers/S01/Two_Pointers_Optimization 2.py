from typing import List
def removeDuplicates(nums: List[int]) -> int:
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1
nums=[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))


from typing import List
def removeElement(nums: List[int], val: int) -> int:
    i=0
    for j in range(len(nums)):
        if nums[j]!=val:
            nums[i]=nums[j]
            i+=1
    return i
nums=[1,4,6,8,2,4,6,4,5,6]
print(removeElement(nums,4))