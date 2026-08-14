class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Count characters in t
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        
        # Variables to track the window
        left = 0
        right = 0
        formed = 0  # How many characters in need are satisfied
        window_counts = {}  # Counts in current window
        
        # Result variables
        min_len = float('inf')
        min_left = 0
        
        while right < len(s):
            # Add character from right side
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if this character helps satisfy a requirement
            if char in need and window_counts[char] == need[char]:
                formed += 1
            
            # Try to shrink the window while it's valid
            while formed == len(need) and left <= right:
                # Update result if this is the smallest window
                curr_len = right - left + 1
                if curr_len < min_len:
                    min_len = curr_len
                    min_left = left
                
                # Remove character from left side
                left_char = s[left]
                window_counts[left_char] -= 1
                
                # If this breaks a requirement, decrement formed
                if left_char in need and window_counts[left_char] < need[left_char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return s[min_left:min_left + min_len] if min_len != float('inf') else ""

            