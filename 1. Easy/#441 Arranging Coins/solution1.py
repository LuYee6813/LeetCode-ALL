def arrangeCoins(n):
    # r: 把第 1 ~ k 層塞滿會用到多少硬幣
    r = 0
    # k: 目前要塞的是第幾層
    k = 1
    while True:
        r += k     
        if r > n:
            return k - 1
        k += 1
            
class Solution:
    def arrangeCoins(self, n:int) -> int:
        return arrangeCoins(n)