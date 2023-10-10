use std::cmp::{min, max};

fn max_product_subarray(nums: &Vec<i32>) -> i32 {
    let mut max_num: i32 = nums[0] as i32;
    let mut now_max: i32 = 1;
    let mut now_min: i32 = 1;

    for num in nums {
        let now_max_multiplied = now_max *num;
        let now_min_multiplied = now_min * num;
        now_max = max(now_max_multiplied, max(*num, now_min_multiplied));
        now_min = min(now_min_multiplied, min(*num, now_min_multiplied));
        max_num = max(now_max, max_num);
    }
    return max_num;
}

fn main(){
    let test_vec = vec![1,-2,1,4,-2,-1];
    println!("{:?}", max_product_subarray(&test_vec));
}