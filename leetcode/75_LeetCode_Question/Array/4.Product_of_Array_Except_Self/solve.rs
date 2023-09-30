fn product_array(nums: &Vec<i32>) -> Vec<i32>{
    let idx: usize = nums.len();
    let mut postfix_prod = 1;
    let mut prefix_prod = 1;
    let mut results: Vec<i32> = vec![0; idx];

    for i in 0..idx {
        results[i] = prefix_prod;
        prefix_prod *= nums[i];
    }
    for i in (0..idx).rev(){
        results[i] *= postfix_prod;
        postfix_prod *= nums[i];
    }
    return results;
}

fn main(){
    let case1: Vec<i32> = vec![1,2,3,4];
    println!("{:?}", product_array(&case1));
}