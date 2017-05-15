class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        "rtype List[int]
        """
        if len(nums) <= 1:
            return False
        # for i in len(nums):
        print nums, target

def main():
    nums = [2, 7, 11, 15]
    target = 9
    Solution(nums, target)

if __name__ == '__main__':
    main()