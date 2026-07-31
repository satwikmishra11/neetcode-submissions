class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> charSet = new HashSet<>();
        int left = 0;
        int maxLength = 0;
        
        for (int right = 0; right < s.length(); right++) {
            // If duplicate found, shrink window from left
            while (charSet.contains(s.charAt(right))) {
                charSet.remove(s.charAt(left));
                left++;
            }
            
            // Add current character
            charSet.add(s.charAt(right));
            
            // Update max length
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
}
