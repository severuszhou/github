import time
def removeElement(nums,val):
    size = 0
    length = len(nums)
    for i in range(length):
        if nums[i]!= val:
            nums[size] = nums[i]
            size += 1
    return size,nums


if __name__ == '__main__':
    start = time.clock()
    arr = [3,2,2,3]
    a,b = removeElement(arr,3)
    print(a,b)
    t = time.clock()-start
    print(t*1000*300)

