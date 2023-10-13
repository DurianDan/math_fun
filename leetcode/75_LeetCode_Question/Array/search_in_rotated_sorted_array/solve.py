def find_target_1(nums, target):
    try: return nums.index(target)
    except: return -1

print(find_target_1([4,5,6,7,8,0,1,2], 6))
