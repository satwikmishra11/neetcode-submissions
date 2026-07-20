class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        # Iterate through the array, fixing the first element
        for i in range(n - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Early break if the smallest element is > 0
            # Since array is sorted, if nums[i] > 0, no triplet can sum to 0
            if nums[i] > 0:
                break
            
            # Two-pointer approach for the remaining two elements
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    # Sum is too small, move left pointer to increase sum
                    left += 1
                else:
                    # Sum is too large, move right pointer to decrease sum
                    right -= 1
        
        return result