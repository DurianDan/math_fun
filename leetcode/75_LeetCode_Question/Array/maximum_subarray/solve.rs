use std::cmp::max;

pub fn max_sub_array(nums: Vec<i32>) -> i32 {
    let (mut now_sum, mut max_sum) = (nums[0],nums[0]);
    for idx in 1..nums.len(){
        now_sum = max(now_sum + nums[idx], nums[idx]);
        max_sum = max(now_sum, max_sum);
    }
    return max_sum;
}

fn main(){
    let cases = vec![
        vec![1,-1,2,-1,4],
        vec![5,4,-1,7,8],
        vec![1],
        vec![-2,1,-3,4,-1,2,1,-5,4]
        ];
    for (idx, case) in cases.iter().enumerate() {
        println!("+ Case {}: {:?} => Result: {:?}", idx, case, max_sub_array(case));
    }
}