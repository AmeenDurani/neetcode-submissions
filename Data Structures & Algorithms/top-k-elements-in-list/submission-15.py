class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) - 1
        
        heap = [(freq, num) for num, freq in count.items()]
        heapq.heapify(heap)

        res = []
        for i in range(k):
            _, num = heapq.heappop(heap)
            res.append(num)
        
        return res
        