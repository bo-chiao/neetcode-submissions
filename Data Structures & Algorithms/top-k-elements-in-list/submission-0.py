class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums))] 
        for key, val in count.items():
            buckets[val - 1].append(key)

        result = []
        for l in reversed(buckets):
            for num in l:
                result.append(num)
                k -= 1
                if k == 0:
                    return result
        