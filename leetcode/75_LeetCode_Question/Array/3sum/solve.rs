# idea1: O(n^2) looping through the array, and also hashmap-ing
use std::collections::HashMap;

fn three_sum(nums: &Vec<i32>, target_sum: i32)-> Vec<i32>{
    let mut table = HashMap::<i32, i32>::new();
    
}