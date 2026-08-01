class Solution {
    public int characterReplacement(String s, int k) {
        int[] charCount = new int[26];
        int maxFreq = 0;
        int left = 0;
        int maxLength = 0;
        
        for (int right = 0; right < s.length(); right++) {
            // Add current character to window
            charCount[s.charAt(right) - 'A']++;
            
            // Update max frequency
            maxFreq = Math.max(maxFreq, charCount[s.charAt(right) - 'A']);
            
            // Shrink window if invalid
            if ((right - left + 1) - maxFreq > k) {
                charCount[s.charAt(left) - 'A']--;
                left++;
                // Note: We don't recalculate maxFreq here because it might be slightly 
                // higher than actual, but this doesn't affect correctness as it only 
                // makes the condition more restrictive temporarily
                // The next iteration will adjust maxFreq as needed
            }
            
            // Update answer
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
}
