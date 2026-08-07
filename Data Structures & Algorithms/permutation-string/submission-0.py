class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        # Frequency arrays for 26 lowercase letters
        s1_count = [0] * 26
        window_count = [0] * 26
        
        # Count characters in s1
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
            
        # Initialize first window
        for i in range(len(s1)):
            window_count[ord(s2[i]) - ord('a')] += 1
            
        # Check first window
        if s1_count == window_count:
            return True
            
        # Slide the window
        for i in range(len(s1), len(s2)):
            # Add new character to window
            window_count[ord(s2[i]) - ord('a')] += 1
            # Remove old character from window
            window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            # Check if current window matches
            if s1_count == window_count:
                return True
                
        return False
        