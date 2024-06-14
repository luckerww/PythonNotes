# class
class MyClass:
    # constructor
    def __init__(self, nums):
        # creating member variables
        self.nums = nums
        self.size = len(nums)

    # self key word required as param
    def getlength(self):
        return self.size

    def getDoublelength(self):
        return 2 * self.getlength()

