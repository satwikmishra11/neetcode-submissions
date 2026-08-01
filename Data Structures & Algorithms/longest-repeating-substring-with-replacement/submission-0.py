class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Frequency map for characters in current window
        char_count = {}
        max_freq = 0
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # Add current character to window
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            
            # Update max frequency in current window
            max_freq = max(max_freq, char_count[s[right]])
            
            # Check if window is valid
            # If window size - max_freq > k, we need to shrink
            while (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1
                
                # Recalculate max_freq for the new window
                # This is O(26) or O(1) since we only have 26 uppercase letters
                max_freq = max(char_count.values()) if char_count else 0
            
            # Update answer
            max_length = max(max_length, right - left + 1)
        
        return max_length
        