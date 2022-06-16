class Solution:
    def average(self, salary: List[int]) -> float:
        max = salary[0]
        min = salary[0]
        c = 0
        for i in salary:
            if (i > max):
                max = i                
            if (i < min):
                min = i
            c+=i
        return (c-min-max) / (len(salary)-2)