fn search_rotated_1(nums: Vec<i32>, target: i32) -> i32 {
    for idx in 0..nums.len(){
        if nums[idx] == target {
            return idx as i32;
        }
    };
    return -1;
}

fn main(){
    println!("{:?}", search_rotated_1(vec![1,2,3,4], 4));
}
