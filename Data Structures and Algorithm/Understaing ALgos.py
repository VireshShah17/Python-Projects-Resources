def maxProduct(nums):
        if not nums:
            return 0

        maximum = minimum = result = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_maximum = max(curr, maximum * curr, minimum * curr)
            minimum = min(curr, maximum * curr, minimum * curr)
            maximum = temp_maximum
            result = max(maximum, result)
        return result


print(maxProduct([2,3,-2,4]))