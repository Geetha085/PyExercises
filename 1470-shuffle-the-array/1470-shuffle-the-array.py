class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
       x=nums[:n]
       y=nums[n:]
       res=[]
       for i ,j in zip(x,y):
        res.append(i)
        res.append(j)
       return res

        