def threeSum(nums):
    nums.sort()
    res = []

    for i in range(len(nums)):
        # 剪枝：如果当前检索的三元组中最小的值>0，直接结束遍历
        if nums[i] > 0:
            return res

        if i > 0 and nums[i - 1] == nums[i]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])

                while (left < right) and (nums[left] == nums[left + 1]):
                    left += 1  # 注意：此时的新left仍然=sum里的nums[旧left]
                while (left < right) and (nums[right] == nums[right - 1]):
                    right -= 1  # 注意：此时的新right仍然=sum里的nums[旧right]

                # 双指针向中间缩，取下一组和res里不同的nums[left]和nums[right]值
                left += 1
                right -= 1

    return res


if __name__ == '__main__':
    # nums = [-3,-3,-2,0,1,2,3,3]
    nums = [0,1,2,3,4]
    print(threeSum(nums))