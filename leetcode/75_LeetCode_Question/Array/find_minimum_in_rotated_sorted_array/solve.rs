fn find_min_1(nums: &Vec<i32>) -> i32 {
    return *nums.iter().min().unwrap();
}

fn find_min_2(nums: &Vec<i32>) -> i32 {
    for idx in 0..(nums.len()-1){
        if nums[idx+1] < nums[idx]{
          return nums[idx+1];
        }
      };
      return nums[0];
}

fn find_min_3(nums: &Vec<i32>) -> i32 {
  let mut l = 0 as usize;
  let mut r = nums.len()-1;

  while l <= r {
    let mid = l + (r-l)/2;
    if nums[mid] < nums[r]{
      r = mid;
    }else{
      l = mid+1;
    }
  }
  return nums[r];
}

fn main(){
    let test_vector = vec![4,5,1,2,3];
    println!("{:?}", find_min_1(&test_vector));
    println!("{:?}", find_min_2(&test_vector));
    println!("{:?}", find_min_3(&test_vector));
}