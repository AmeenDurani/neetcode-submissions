class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        heap = []

        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        # currently, dictionary items, if made tuple, would be (num, freq)...
        # but to use min/max heap, we need to have (freq, num).
        for (num, freq) in d.items():
            heapq.heappush(heap, (-freq, num))
        
        res = []
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
        
        return res

