class Solution:
    def reverseBits(self, n: int) -> int:
        return int(''.join(reversed((bin(n)[2: ]).zfill(32))), 2)