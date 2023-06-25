class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] > target or nums[-1] < target:
            return -1
        elif nums[0] == target:
            return 0
    
        low = 0
        high = len(nums) - 1
    
        while (high - low) > 1:
            print("high" + str(high),"low" + str(low))
    
            if nums[ceil((high + low) / 2)] >= target:
                high = ceil((high + low) / 2)
            elif nums[ceil((high + low) / 2)] < target:
                low = ceil((high + low) / 2)
        
        if nums[high] == target:
            return high
        elif nums[low] == target:
            return low    
        return -1
