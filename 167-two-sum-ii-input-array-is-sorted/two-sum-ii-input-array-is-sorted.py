class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        L = []
        right = len(numbers)-1

        while left<right:
            if numbers[left] + numbers[right] > target : 
                right -= 1
            elif numbers[left] + numbers[right] < target : 
                left += 1
            else:
                L.append(left+1)
                L.append(right+1)
                return L