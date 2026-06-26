class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Sort by frequency in descending order and get the top k
        result = []
        for num, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            result.append(num)
            if len(result) == k:
                break
        
        return result