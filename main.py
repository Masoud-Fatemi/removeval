class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        length = len(nums)
        j = 0

        for i in xrange(length):

            if nums[j] == val:
                del nums[j]
            else:
                j += 1

        return j