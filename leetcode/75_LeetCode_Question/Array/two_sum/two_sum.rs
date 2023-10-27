use std::collections::HashMap;

fn two_sum(nums: &Vec<i32>, target: i32) -> Vec<i32> {
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

fn two_sum_hashmap(nums: &Vec<i32>, target: i32) -> Vec<i32>{
    let mut table = HashMap::<i32, i32>::new();
    for (idx, num) in nums.iter().enumerate(){
        match table.get(&(target-num)) {
            Some(remainer_idx) => {
                return vec![idx as i32, *remainer_idx]
            },
            None => {table.insert(*num, idx as i32)}
        };
    }
    return vec![];
}

fn main(){
    let test_num: i32 = 12;
    let test_vec = vec![1,2,3,4,5,6,7,8];

    println!("two_sum {:?}", two_sum(&test_vec, test_num));
    println!("two_sum_hashmap {:?}", two_sum_hashmap(&test_vec, test_num));
}
