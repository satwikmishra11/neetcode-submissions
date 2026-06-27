class Solution:
    def encode(self, strs):
        """
        Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    
    def decode(self, s):
        """
        Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        decoded = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            
            start = j + 1
            end = start + length
            decoded.append(s[start:end])
            
            i = end
        
        return decoded