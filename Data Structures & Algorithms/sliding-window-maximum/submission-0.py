class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        n = len(nums)
        result = []
        dq = deque()  # stores indices
        
        for i in range(n):
            # Remove indices outside current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove indices of smaller elements from back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            
            # Add current index
            dq.append(i)
            
            # Add to result when window is complete
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result