class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1, ptr2 = 0, 1
        while ptr1 < len(numbers) - 1:
            if numbers[ptr1] + numbers[ptr2] == target:
                return [ptr1+1, ptr2+1]
            
            elif numbers[ptr1] + numbers[ptr2] < target:
                ptr2 += 1
                if ptr2 >= len(numbers):
                    ptr1 += 1
                    ptr2 = ptr1 + 1

            else:
                ptr1 += 1
                ptr2 = ptr1 + 1

            