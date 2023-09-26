fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let nums_length: usize = nums.len();
    for (idx, num) in nums[..nums_length-1].iter().enumerate(){
        for next_idx in (idx+1)..nums_length{
            if nums[next_idx] + num == target{
                return vec![idx as i32, next_idx as i32];
            }
        }
    }

    // Return an empty vector if no solution is found
    vec![]
}

fn main(){
    let test_num: i32 = 12;
    let test_vec = vec![1,2,3,4,5,6,7,8];

    let result: Vec<i32> = two_sum(test_vec, test_num);
    println!("{:?}", result);
}
