class Solution:

    def __init__(self, w: List[int]):
        
        self.__w = w
        # 累積圖
        # a[0] = w[0]
        # a[1] = a[0] + w[1]
        # a[2] = a[1] + w[2]
        
        a = [None] * len(w)
        a[0] = w[0]
        for i in range(1, len(w)):
            a[i] = a[i-1] + w[i]
        self.__a = a
        print(a)
        

    def pickIndex(self) -> int:
        d = random.randrange(self.__a[-1])
        
        for i, c in enumerate(self.__a):
            if d < c:
                return i    
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()