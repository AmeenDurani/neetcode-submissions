class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        h = []
        for num, freq in d.items():
            heapq.heappush(h, (-freq, num))

        r = []
        for _ in range(k):
            _, num = heapq.heappop(h)
            r.append(num)
        
        return r
