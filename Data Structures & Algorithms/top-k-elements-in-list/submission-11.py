class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in d.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                if len(res) == k:
                    return res
                res.append(j)
        return res
