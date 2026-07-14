class Solution {
    public boolean isPalindrome(String s) {
    String lowerStr = s.toLowerCase();
        
        int left = 0;
        int right = lowerStr.length() - 1;
        
        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(lowerStr.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(lowerStr.charAt(right))) {
                right--;
            }
            
            if (lowerStr.charAt(left) != lowerStr.charAt(right)) {
                return false;
            }
            
            left++;
            right--;
        }
        
        return true;
    }
}