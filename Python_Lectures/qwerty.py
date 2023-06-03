def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0


nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print(nums)  # [3, 9, 10, 27, 38, 43, 82]
