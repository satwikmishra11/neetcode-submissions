class Solution {
    public int maxArea(int[] heights) {
        // Initialize two pointers at the ends
        int left = 0;
        int right = heights.length - 1;
        int maxWater = 0;
        
        // Continue until pointers meet
        while (left < right) {
            // Calculate current area
            int width = right - left;
            int currentHeight = Math.min(heights[left], heights[right]);
            int currentArea = width * currentHeight;
            
            // Update max water if current area is larger
            maxWater = Math.max(maxWater, currentArea);
            
            // Move the pointer pointing to the shorter bar
            // This gives us a chance to find a taller bar and potentially larger area
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        return maxWater;
    }
}