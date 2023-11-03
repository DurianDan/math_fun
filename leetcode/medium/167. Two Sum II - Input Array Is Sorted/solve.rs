pub fn two_sum_two_pointers(numbers: Vec<i32>, target: i32) -> Vec<i32> {
    let mut l: i32 = 0;
    let mut r: i32 = numbers.len() as i32 - 1;
    while l <= r {
        let num_r = numbers[r as usize];
        let num_l = numbers[l as usize];
        let tmp_sum = num_r + num_l;
        if tmp_sum == target{
            return vec![l+1, r+1];
        }else if tmp_sum > target{
            r -= 1;
        }else{ l+= 1}
    };
    return vec![];
}

fn main(){
    let test_vect = vec![1,2,3,4];
    let test_target = 5;
    println!("{:?}", two_sum_two_pointers(test_vect, test_target))
}