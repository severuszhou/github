def searchInsert(nums, target):
    if target in nums:
        for i in nums:
            if i == target:
                return nums.index(i)
    else:
        j = 0
        for i in nums:
            if i < target:
                j += 1
        return j


if __name__ == '__main__':
    a = searchInsert([1,3,5,6] ,0.5)
    print(a)

