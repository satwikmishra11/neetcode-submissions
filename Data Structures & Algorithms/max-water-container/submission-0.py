class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize two pointers at the ends
        left = 0
        right = len(heights) - 1
        max_water = 0
        
        # Continue until pointers meet
        while left < right:
            # Calculate current area
            width = right - left
            current_heights = min(heights[left], heights[right])
            current_area = width * current_heights
            
            # Update max water if current area is larger
            max_water = max(max_water, current_area)
            
            # Move the pointer pointing to the shorter bar
            # This gives us a chance to find a taller bar and potentially larger area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_water
        