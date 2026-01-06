class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # If k is even or divisible by 5, no solution exists
        # (111...1 is always odd and never ends in 0 or 5)
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        # Use modular arithmetic
        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
        
        return -1