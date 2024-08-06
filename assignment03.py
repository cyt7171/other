class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if(len(nums)<=1):
            return nums
        mid = int(len(nums)/2)
        ##llist = self.sortArray(nums[:mid])  
        ##rlist = self.sortArray(nums[mid:])
        llist,rlist = self.sortArray(nums[:mid]),self.sortArray(nums[mid:])
        result = []
        i,j = 0,0
        while i < len(llist) and j < len(rlist):
            if rlist[j] < llist[i]:
                result.append(rlist[j])
                j +=1
            else:
                result.append(llist[i])
                i +=1
        result += llist[i:]+rlist[j:]
        return result 
