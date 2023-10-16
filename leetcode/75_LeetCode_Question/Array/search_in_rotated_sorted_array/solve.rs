fn search_rotated_1(nums: &Vec<i32>, target: i32) -> i32 {
    for idx in 0..nums.len(){
        if nums[idx] == target {
            return idx as i32;
        }
    };
    return -1;
}

fn binary_search_rotated(nums: &Vec<i32>, target: i32) -> i32 {
    let mut r = nums.len()-1;
    let mut l = 0;
    let mut mid: usize;
    while l <= r {
        mid = l + (r-l)/2;
        if target == nums[mid]{
            return mid as i32;
        };

        if nums[mid] >= nums[l] {
            if target > nums[mid] || target < nums[l]{
                l = mid + 1;
            }else{
                r = mid - 1;
            }
        }else{
            if target < nums[mid] || target > nums[r]{
                r = mid - 1;
            }else{
                l = mid + 1;
            }
        }
    }
    return -1;
}

fn main(){
    let test_vec = vec![4,5,6,7,8,9,10,1,2,3];
    let test_target = 1;
    println!("search_rotated_1: {:?}", search_rotated_1(&test_vec, test_target));
    println!("binary_search_rotated: {:?}", binary_search_rotated(&test_vec, test_target));
}
