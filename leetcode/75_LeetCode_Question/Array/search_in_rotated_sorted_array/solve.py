def find_target_1(nums, target):
    try: return nums.index(target)
    except: return -1

def binary_search_rotated(nums, target):
    r,l = len(nums) -1, 0
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] == target: return mid
        if nums[mid] >= nums[l]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else: 
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1

test_arr = [4,5,6,7,8,0,1,2]
test_target = 1
print(find_target_1(test_arr, test_target))
print(binary_search_rotated(test_arr, test_target))
